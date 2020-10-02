from tqdm import tqdm
import requests


chunk_size = 256
url = "https://www66.zippyshare.com/d/gWpccIz4/534/Haikyuu_2_01_Ichiban-Anbient.mkv"

r = requests.get(url, stream=True)

total_size = int(r.headers["content-length"])

with open("test11.mp4", "wb") as f:
    for data in tqdm(
        iterable=r.iter_content(chunk_size=chunk_size),
        total=total_size / chunk_size,
        unit="KB",
    ):
        f.write(data)

print("Download complete!")
