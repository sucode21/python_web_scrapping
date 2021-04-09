import requests
from bs4 import BeautifulSoup

url="https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
resp=requests.get(url)
html_src=resp.text

soup=BeautifulSoup(html_src,"html.parser")

subway_img=soup.select('#mw-content-text > div.mw-parser-output > table:nth-child(3) > tbody > tr:nth-child(2) > td > a > img')
print(subway_img)
print("\n")

print(subway_img[0])
print("\n")

