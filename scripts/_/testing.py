import pytube

import urllib.request
import subprocess

content = pytube.YouTube('https://www.youtube.com/watch?v=Ahha3Cqe_fk')
streams = content.streams.filter(only_audio=True).order_by("abr").desc()
response = urllib.request.urlopen(streams[0].url)

def download_and_convert_parallely():
    command = ("ffmpeg", "-y", "-i", "-", "output.wav")
    process = subprocess.Popen(command, stdin=subprocess.PIPE)

    while True:
        chunk = response.read(16 * 1024)
        if not chunk:
            break
        process.stdin.write(chunk)

    process.stdin.close()
    process.wait()


download_and_convert_parallely()
