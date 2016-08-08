import json
import datetime
import urllib.parse
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_keys import *
import mysql.connector
import api.eventall2016_credentials

# Variables that contains the user credentials to access Twitter API
# consumer_key = 'api_key'
# consumer_secret = 'api_secret'
# access_token = 'access_token'
# access_token_secret = 'access_token_secret'


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)

        post_status = db_post(json.loads(data))

        if post_status:
            return True
        else:
            with open('twitter_stream_errors.json', 'a') as file:
                file.write(data)

        return True

    def on_error(self, status):
        print(status)


def tweet_feed(stream_array):
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    print('Starting stream...')
    stream.filter(locations=stream_array)


def db_post(data):
    data['data'] = json.dumps(data).replace('"', "''")
    data['text'] = urllib.parse.quote(data['text'])
    data['created_at'] = datetime.datetime.strptime(
        data['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d %H:%M:%S')
    config = api.eventall2016_credentials.eventall2016_credentials()

    query = '''INSERT INTO twitter2016 (tweet_timestamp, tweet_text, tweet_json)
    VALUES ("{created_at}", "{text}", "{data}");'''.format(**data)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute(query)
        cnx.commit()
        status = True

    except mysql.connector.Error as e:
        cnx.rollback()
        status = False

    finally:
        cursor.close()
        cnx.close()

    print('Post status: ' + str(status))

    return status


if __name__ == '__main__':
    tweet_feed([-122.342377, 47.382283, -122.270966, 47.775070])
