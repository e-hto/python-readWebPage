import requests

from bs4 import BeautifulSoup

url = 'https://www.smbc-comics.com/index.php' # Enter url here

r = requests.get(url)

html = r.text

soup = BeautifulSoup(html, "lxml")

title = soup.find('span', 'articletitle')

print(html)
