import requests
from bs4 import BeautifulSoup as bs

url = "https://www26.zippyshare.com/v/05CQX11J/file.html"
irl = "https://www26.zippyshare.com/v/05CQX11J/file.html"

r = requests.get(url)

soup = bs(r.text, "lxml")

list_ = soup.find_all("div", class_="lrbox")

print(list_)
