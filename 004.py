import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp=requests.get(url)
html_src=resp.text

soup=BeautifulSoup(html_src,"html.parser")
print(type(soup))
print(soup.head)
print(soup.body)
print(soup.title)
print(soup.title.string)
