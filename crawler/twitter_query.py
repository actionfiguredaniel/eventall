from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twitter_keys import *

# Variables that contains the user credentials to access Twitter API
# consumer_key = 'api_key'
# consumer_secret = 'api_secret'
# access_token = 'access_token'
# access_token_secret = 'access_token_secret'


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('twitter_stream.json', 'a') as file:
            file.write(data + ',')

        print(data)
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


if __name__ == '__main__':
    tweet_feed([-122.342377, 47.382283, -122.270966, 47.775070])
