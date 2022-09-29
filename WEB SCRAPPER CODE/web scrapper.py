import html
from bs4 import BeautifulSoup
import requests
import pandas as pd
import json 
response = requests.get("https://www.dawn.com/")
soup = BeautifulSoup(response.text, 'lxml')
temp=soup.findAll("h2")
#soup = BeautifulSoup(response.content, 'html5lib')
#print(soup.prettify())

# creat list of heading tags
for tags in temp:
    headings=tags.text.strip()
    print(headings)