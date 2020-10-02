import os
import subprocess
import re
from pytube import YouTube, Playlist


path = r'DESTINATION_FOLDER'
playlist_url = 'PLAYLIST_URL'

play = Playlist(playlist_url)

play._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(len(play.video_urls))
for url in play.video_urls:
    yt = YouTube(url)
    audio = yt.streams.get_audio_only()
    audio.download(path)
    name = yt.title
    new_filename= name + '.mp3'
    default_filename = name + '.mp4'
    ffmpeg = (f'ffmpeg -i {default_filename} {new_filename}')
    subprocess.run(ffmpeg, shell=True)

print('Download Complete')
