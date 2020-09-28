# from bs4 import BeautifulSoup as bs
# import requests


# r = requests.get(url)
# page = r.text
# soup = bs(page, 'html.parser')

# res = soup.find_all('a', {'class': 'pl-video-title-link'})
# for l in res:
#     print(l.get("href"))


# from bs4 import BeautifulSoup
# import requests


# def getPlaylistLinks(url):
#     sourceCode = requests.get(url).text
#     soup = BeautifulSoup(sourceCode, 'html.parser')
#     domain = 'https://www.youtube.com'
#     for link in soup.find_all("a", {"dir": "ltr"}):
#         href = link.get('href')
#         if href.startswith('/watch?'):
#             print(link.string.strip())
#             print(domain + href + '\n')


# url = 'https://www.youtube.com/watch?v=2rEZYrbXAhU&list=UUK5tosXMdCitAX8ef7j5c9w&index=1'


# getPlaylistLinks(url)
