#/usr/bin/python3
# Get links by accessing url
from selenium import webdriver
import time
import numpy as np
#import requests
from bs4 import BeautifulSoup
import io
import re


browser = webdriver.Chrome()
browser.get("https://www.catalog.update.microsoft.com/Search.aspx?q=KB4598457")

elem = browser.find_element_by_xpath('//*[@id="151315e6-b978-42fc-b0ce-6e5c78a69324"]')
elem.click()
time.sleep(0.2)

elem = browser.find_element_by_xpath("//*")
# show main page html
print(elem.get_attribute("outerHTML"))
####################################################
soup = BeautifulSoup(elem, 'html.parser')
elems = soup.find_all(href=re.compile("/a/"))
links = []
for i in range(len(elems)):
    links.append('test'+elems[i].attrs['href'])
links = np.unique(links)
text='\n'.join(links)
with io.open('article-url.txt', 'w', encoding='utf-8') as f:
    f.write(text)

