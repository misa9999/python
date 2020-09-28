import requests
from bs4 import BeautifulSoup as bs


url = ""
r = requests.get(url)

parser = bs(r.text, 'lxml')
print(parser)
