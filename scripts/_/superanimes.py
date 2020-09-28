#https://www.superanimes.org/anime/hunter-x-hunter-2011/1011{}/baixar

#import requests

#chunk_size = 256

#url = "https://r1---sn-4g5e6nsz.googlevideo.com/videoplayback?expire=1599142926&ei=jotQX9C3EIWGhgaCqZTIBQ&ip=2a01:4f8:160:834c::2&id=5875cce5863a1736&itag=18&source=blogger&mh=oh&mm=31&mn=sn-4g5e6nsz&ms=au&mv=m&mvi=1&pl=47&susc=bl&mime=video/mp4&dur=1417.322&lmt=1323587993851599&mt=1599114037&sparams=expire,ei,ip,id,itag,source,susc,mime,dur,lmt&sig=AOq0QJ8wRAIgOFUKeJQHAmHWqEpd4_DRJAgbBpJOOM8blhOjNVy4FFECIEiw-3eXGEHCwEw0Q7k0RT_sbklCUF9MCbnZbnzauN1k&lsparams=mh,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhAI1PNUWFthVLAS3CMyQNm-n6DFPqNoodxajR7A_uyN6lAiBSlONxgVMyOG2NDzQ6SNSMbwVqtcrQ1AlBUXbTM71Uww%3D%3D"

#r = requests.get(url, stream=True)

#with open("Hunter-x-hunter-2011_11.mp4", "wb") as f:
    #for chunk in r.iter_content(chunk_size=chunk_size):
        #f.write(chunk)


import requests
from bs4 import BeautifulSoup as bs

url = "https://www.superanimes.org/anime/hunter-x-hunter-2011/10116"
r = requests.get(url)

parser = bs(r.text, 'lxml')
print(parser)


#video_list = soup.find_all('div', class_='contentVideo')
#print(video_list)














