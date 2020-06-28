# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:46:05 2020

@author: User
"""


import requests
from bs4 import BeautifulSoup 

BASE_URL = "https://ca.finance.yahoo.com"
PRICE_URL = "https://ca.finance.yahoo.com/quote/"

my_tickers = ['QUIS.V', 'TD.TO', 'XOM', 'WFC', 'AAPL', 'GOOG']

for ticker in my_tickers:
  URL = PRICE_URL + ticker + '/news'
  r = requests.get(URL) 

  soup = BeautifulSoup(r.content, 'html5lib') 

  price_header = soup.find('div', attrs = {'id':'quote-header-info'})
  price = price_header.find_all('span')[1].text
  print(ticker + "'s current price: " + price)

  news_container = soup.find('ul', attrs = {'data-reactid':'3'})
  articles = news_container.findChildren('li', recursive=False)
  print('Articles for ' + ticker)

  for article in articles[:3]:
    article_url = article.find('div').find('div').findChildren('div')[2].findChildren('a', href=True)[0]['href']

    r = requests.get(BASE_URL + article_url)
    soup = BeautifulSoup(r.content, 'html5lib') 

    article_title = soup.find('div', attrs = {'id':'YDC-Side-StackCompositeSideTop'}).find_all('h1')[0].text
    print (article_title)

  print('\n---\n')