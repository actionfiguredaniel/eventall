from bs4 import BeautifulSoup
import urllib3
import sys
sys.path.append('D:\dkeva\Documents\GitHub\eventall\api')

from eventall2016_credentials import *


def connect_web(url):
    try:
        http = urllib3.PoolManager()
        http.headers = urllib3.make_headers(user_agent=None)
        html = http.urlopen('GET', url)
        return html
    except ValueError:
        print("{}... does not exist..".format(url))


def main():
    data_list = []
    months = [
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'november',
        'december'
    ]
    for month in months:
        url = 'http://www.events12.com/seattle/{0}/'.format(month)
        x = connect_web(url)
        soup = BeautifulSoup(x.data, 'html5lib')
        title = soup.find_all('p', attrs={"class": "title"})
        date = soup.find_all('p', attrs={"class": "date"})
        for i in range(len(title)):
            description = title[i].parent.text
            name = title[i].text
            datetime = date[i].text
            data_list.append([name.replace("\n", "").replace("'", "\'"), datetime.replace("\n", "").replace("'", "\'"),
                              description.replace("\n", "").replace("'", "\'")])
            print(data_list[i])

    for row in data_list:
        payload = {'event_name': row[0],
                   'event_date': row[1],
                   'event_description': [2]
                   }
        write_event(payload)


if __name__ == "__main__":
    main()
