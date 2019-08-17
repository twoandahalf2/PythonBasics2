import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.devdungeon.com/archive')

soup = BeautifulSoup(response.text)

# print(soup.prettify())
print(soup.title)
print(soup.title.string)
for a in soup.find_all('a'):
    print(a.get('href'))