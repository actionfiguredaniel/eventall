from bs4 import BeautifulSoup
import urllib3, requests, re, csv, sys, os, time, html5lib, mysql.connector
import eventall_credentials

def connectWeb(url):
    try:
        http = urllib3.PoolManager()
        http.headers = urllib3.make_headers(user_agent=None)
        html = http.urlopen('GET', url)
        soup = BeautifulSoup(html.data, 'html5lib')
        return html
    except Exception as e:
        print ("{}... does not exist..".format(url))
        
def main():
    dataList = []
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
        x = connectWeb(url)
        soup = BeautifulSoup(x.data, 'html5lib')
        title = soup.find_all("p",attrs={"class":"title"})
        date = soup.find_all("p",attrs={"class":"date"})
        for i in range(len(title)):
            description = title[i].parent.text
            name = title[i].text
            datetime = date[i].text
            dataList.append([name.replace("\n", "").replace("'","\'"),datetime.replace("\n", "").replace("'","\'"),description.replace("\n", "").replace("'","\'")])
            print (dataList[i])

    #connecting to MySQL
    config = eventall_credentials()

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    for row in dataList:
        query = 'insert into eventall2016(event_name,event_date,event_description) values ("{0}","{1}","{2}")'.format(row[0], row[1], row[2])
        print(query)
        cursor.execute(query)
        cnx.commit()


if __name__ == "__main__":
    main()