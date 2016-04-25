from bs4 import BeautifulSoup
import urllib3, requests, re, csv, sys, os, time, html5lib

def connectWeb(url):
    dataList = []
    infoList=[]
    infoList.append(url)
    try:
        http = urllib3.PoolManager()
        http.headers = urllib3.make_headers(user_agent=None)
        html = http.urlopen('GET', 'http://www.events12.com/seattle/')
        soup = BeautifulSoup(html.data, 'html5lib')
        title = soup.find_all("p",attrs={"class":"title"})
        date = soup.find_all("p",attrs={"class":"date"}) 
        print (len(title))
        for i in range(len(title)):
            description = title[i].parent.text
            dataList.append([title[i].text,date[i].text,description])
            print (dataList[i])
        return dataList
    except Exception as e:
        print ("{}...{} does not exist..".format(infoList,url))
url = 'http://www.events12.com/seattle/january/'
x = connectWeb(url)






