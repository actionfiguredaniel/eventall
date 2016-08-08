import mysql.connector
from eventall2016_credentials import *


def query_read_city_event(payload):
    config = eventall2016_credentials()
    results = {'status': False}
    if payload['city'] is '' or payload['city'] is None:
        results['error'] = 'A city was not provided with the search results, please try again.'
    else:
        filter_city = 'and lower(city) =lower({city}) '.format(payload['city'])
    if payload['date'] is '':
        filter_date = 'and date between curdate() and curdate() + interval 30 day'
    else:
        filter_date = 'and date = {date}'.format(payload['date'])
    query = 'select * from eventall where 1=1 ' + filter_city + filter_date

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
    query_read_city_event(payload={'city':'Seattle','date':''})

