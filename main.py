#Here we can perform extract only the article title and article tetxs.

# install and import pandas as pd
# install and import requets
# install and import beautifulsoup
import pandas as pd
import requests
from bs4 import BeautifulSoup
import html5lib

url='https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2'
r= requests.get(url)
# print(r)
soup= BeautifulSoup(r.text,'html.parser')
# print(soup)
article_texts= soup.find_all('div', class_= 'td-post-content tagdiv-type')
print(article_texts)
