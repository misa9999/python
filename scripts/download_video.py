import requests

chunk_size = 256
url = input('[*] Enter URL: ')

r = requests.get(url, stream=True)

# path = input('[*] Enter Path: ')
filename = input('[*] Enter Filename: ')
with open(filename+'.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)

