import requests
import os

url = "https://www66.zippyshare.com/d/gWpccIz4/534/Haikyuu_2_01_Ichiban-Anbient.mkv"


def download_file(url, address):
    response = requests.get(url)
    
    if response.status_code == requests.codes.OK:
        with open(address, 'wb') as new_file:
            new_file.write(response.content)
    else:
        response.raise_for_status()

if __name__ == "__main__":
    download_file(url, 'test.mp4')
