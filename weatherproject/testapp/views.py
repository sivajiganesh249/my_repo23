from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
import datetime


#web scraping

url = 'https://www.timeanddate.com/weather/'
res = requests.get(url).content
soup = BeautifulSoup(res,'html.parser')

#home view
def home(requests,soup=soup):
    date = datetime.datetime.today().date
    data = soup.find('span',class_='my-city__city')
    data1 = soup.find('span',class_='my-city__temp')
    data2 = soup.find('span',class_='my-city__wtdesc')
    data3 = soup.find('span',class_='my-city__time-wrap')




    city = data.text
    temp = data1.text
    condition = data2.text
    time = data3.text

    return render(requests,'index.html',{'city':city,'temp':temp,'condition':condition,'date':date,'time':time})
