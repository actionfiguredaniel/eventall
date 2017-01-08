import mysql.connector
from eventall2016_credentials import *


def query_runner():
    config = eventall2016_credentials()

    query = '''
SELECT CAST('tweet_timestamp' AS DATE) DATE, COUNT(*) AS count
FROM  'twiter2016'
GROUP BY CAST('tweet_timestamp' AS DATE)
ORDER BY CAST('tweet_timestamp' AS DATE)
;'''
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        status = True

    except mysql.connector.Error as e:
        status = False

    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    query_runner()
