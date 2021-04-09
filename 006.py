import requests,re
from bs4 import BeautifulSoup

url="https://ko.wikipedia.org/wiki/%ED%8C%8C%EC%9D%B4%EC%8D%AC"
resp=requests.get(url)
html_src=resp.text

soup=BeautifulSoup(html_src,"html.parser")

links=soup.find_all(name="a")
print(len(links))
print("\n")

wiki_link=soup.find_all(name="a",href=re.compile("/wiki/"),limit=3)



