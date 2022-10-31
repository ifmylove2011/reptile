from bs4 import BeautifulSoup
from urllib import request
import re

url = "http://quotes.toscrape.com/"
req = request.Request(url)
responese = request.urlopen(req)
html = responese.read().decode('utf-8')
soup = BeautifulSoup(html, 'lxml')
# print(soup.prettify())

print(soup.title.name)
print(soup.title.string)

for dd in soup.find_all('span','text'):
    print(dd.string)


# print(soup.get_text())
