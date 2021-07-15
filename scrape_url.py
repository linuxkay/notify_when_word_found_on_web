import numpy as np
import requests
from bs4 import BeautifulSoup
import io
import re
url = 'https://learningenglish.voanews.com/z/3521'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
elems = soup.find_all(href=re.compile("/a/"))
links = []
for i in range(len(elems)):
    links.append('https://learningenglish.voanews.com'+elems[i].attrs['href'])
links = np.unique(links)
text='\n'.join(links)
with io.open('article-url.txt', 'w', encoding='utf-8') as f:
    f.write(text)
