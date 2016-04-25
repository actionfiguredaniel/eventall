from bs4 import BeautifulSoup
import urllib3, requests, re, csv, sys, os, time, html5lib, mysql.connector

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
    url = 'http://www.events12.com/seattle/january/'
    x = connectWeb(url)
    soup = BeautifulSoup(x.data, 'html5lib')
    title = soup.find_all("p",attrs={"class":"title"})
    date = soup.find_all("p",attrs={"class":"date"})
    for i in range(len(title)):
        description = title[i].parent.text
        dataList.append([title[i].text,date[i].text,description])
        print (dataList[i])

if __name__ == "__main__":
    main()
#connecting to MySQL
-------------------------------------
config = {
  'user': 'Eventall2016',
  'password': 'cuteF!re77',
  'host': 'eventall.db.5516970.hostedresource.com',
  'database': 'eventall',
  'raise_on_warnings': True,
}

cnx = mysql.connector.connect(**config)




