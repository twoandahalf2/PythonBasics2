import requests

from bs4 import BeautifulSoup

result = requests.get('https://www.google.com/')
print(result.status_code)

src = result.content

soup = BeautifulSoup(src)

links = soup.find_all('a')
print(links)
print('\n')