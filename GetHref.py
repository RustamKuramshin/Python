# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup

url = # URL страницы для парсинга

res = urllib.request.urlopen(url).read()

soup = BeautifulSoup(res)
 
for link in soup.find_all('a'):
    s = link.get('href')
    print(s)
 
