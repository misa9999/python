import os
import sys
import subprocess
import fnmatch

from pytube import YouTube


class Mp3:
    def __init__(self, url):
        self.yt_url = url
        self.audio_filesize = None

    def download_music(self):
        try:
            audio = YouTube(self.yt_url)
        except Exception as e:
            print(
                f"Error. Check your:\n \
                  -connection\n-url is a Youtube url\n\nTry again."
            )
            print("Error:", e)

        audio_type = audio.streams.filter(only_audio=True).first()

        title = audio.title

        print(f"[+] Fetching: {title}...")
        self.audio_filesize = audio_type.filesize

        # starts the download process
        audio_type.download(self.file_path())

        print()
        print(f"[+] {title} Has Been Successfully Downloaded.")

        self.convert(self.file_path())

    def file_path(self):
        home = os.path.expanduser("~")
        download_path = os.path.join(home, "Downloads/Music")
        return download_path

    def convert(self, path):
        for root, folders, files in os.walk(path):
            for file in files:
                if not fnmatch.fnmatch(file, "*.mp4"):
                    continue

                complete_path = os.path.join(root, file)
                file_name, file_extension = os.path.splitext(complete_path)

                mp4_file = file_name + ".mp4"
                mp3_file = file_name + ".mp3"

                if not os.path.isfile(mp4_file):
                    continue

                try:
                    subprocess.call(
                        [
                            "ffmpeg",
                            "-i",
                            os.path.join(path, mp4_file),
                            os.path.join(path, mp3_file),
                            "-v",
                            "-8",
                        ]
                    )
                except Exception as e:
                    print("error:", e)

    # @staticmethod
    # def get_terminal_size():
    #     rows, columns = os.popen("stty size", "r").read().split()
    #     return int(rows), int(columns)

    # @staticmethod
    # def display_progress_bar(bytes_received, filesize, ch="█", scale=0.55):
    #     _, columns = get_terminal_size()
    #     max_width = int(columns * scale)

    #     filled = int(round(max_width * bytes_received / float(filesize)))
    #     remaining = max_width * -filled
    #     bar = ch * filled + " " * remaining
    #     percent = round(100.0 * bytes_received / float(filesize), 1)
    #     text = " ↳ |{bar}| {percent}%\r".format(bar=bar, percent=percent)
    #     sys.stdout.write(text)
    #     sys.stdout.flush()

    # def on_progress(self, chunk, file_handle, bytes_remaining):
    #     audio_filesize
    #     bytes_received = audio_filesize - bytes_remaining
    #     self.display_progress_bar(bytes_received, audio_filesize)


URL = input("url: ")
mp3 = Mp3(URL)
mp3.download_music()
