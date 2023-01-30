import pandas as pd
from bs4 import BeautifulSoup
import requests

f = requests.get('http://quotes.toscrape.com/')
soup = BeautifulSoup(f.text, "lxml")  # "lxml" or "html.parser"
# print(soup.get_text())

quotes = []
authors = []
tags = []

# for i in soup.findAll("div", {"class": "quote"}):
#     print((i.find("span", {"class": "text"})).text)
# for i in soup.findAll("div", {"class": "quote"}):
#     print((i.find("small", {"class": "author"})).text)
# for i in soup.findAll("div", {"class": "quote"}):
#     print((i.find("meta", {"class": "keywords"}))['content'])

for pages in range(1, 10):
    f = requests.get('http://quotes.toscrape.com/page/' + str(pages))
    soup = BeautifulSoup(f.text, "lxml")
    for i in soup.findAll("div", {"class": "quote"}):
        quotes.append((i.find("span", {"class": "text"})).text)
    for j in soup.findAll("div", {"class": "quote"}):
        authors.append((j.find("small", {"class": "author"})).text)
    for k in soup.findAll("div", {"class": "tags"}):
        tags.append((k.find("meta", {"class": "keywords"}))['content'])

finaldf = pd.DataFrame({
    'Quotes': quotes,
    'Authors': authors,
    'Tags': tags
})
print(finaldf)
