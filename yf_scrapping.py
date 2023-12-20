import requests
from bs4 import BeautifulSoup

r = requests.get ("https://finance.yahoo.com/quote/TSLA/")
soup= BeautifulSoup(r.text,"lxml")
print (soup)