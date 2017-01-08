import mysql.connector
from eventall2016_credentials import *


def write_event(payload):
    config = eventall2016_credentials()
    results = {'status': False}

    query = '''
insert into eventall2016(event_name, event_date, event_description)
values ("{event_name}","{event_date}","{event_description}")'''.format(**payload)
    print(query)

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        results['status'] = True

    except SystemError as e:
        connection.rollback()
        results['status'] = False
        results['error'] = e

    finally:
        cursor.close()
        connection.close()

    return results

if __name__ == '__main__':
    write_event(payload)
