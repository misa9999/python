from tqdm import tqdm
import requests


class Download:
    def __init__(self):
        self.chunk_size = 256
        self.url = "https://www66.zippyshare.com/d/gWpccIz4/534/Haikyuu_2_01_Ichiban-Anbient.mkv"
        self.response = requests.get(self.url, stream=True)
        self.total_size = int(self.response.headers["content-length"])

    def download(self):
        filename = "Haikyuu_S02E01"
        with open(filename + ".mp4", "wb") as f:
            for data in tqdm(
                iterable=self.response.iter_content(chunk_size=self.chunk_size),
                total=self.total_size / self.chunk_size,
                unit="KB",
            ):
                f.write(data)

        print("Download complete!")


d = Download()
d.download()
