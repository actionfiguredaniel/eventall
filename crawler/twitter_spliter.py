import json
import datetime
import urllib.parse
import mysql.connector
from eventall2016_credentials import *


def tweet_spliter():
    f = open('twitter_stream.json', 'r+')
    d = f.readlines()
    --f.seek(0)
    count = 0
    for data in d:
        if count >= 700000:
            data = data.strip(',')

            if len(data) < 2:
                continue

            print('\n' + str(count))

            try:
                json_data = json.loads(data)
            except:
                continue

            post_status = db_post(json_data)

            if not post_status:
                with open('twitter_stream_errors.json', 'a') as file:
                    file.write(data)

        count += 1
    f.truncate()
    f.close()


def db_post(data):
    data['data'] = json.dumps(data).replace('"', "''")
    data['text'] = urllib.parse.quote(data['text'])
    data['created_at'] = datetime.datetime.strptime(
        data['created_at'], '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d %H:%M:%S')
    config = eventall2016_credentials()

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
    tweet_spliter()
