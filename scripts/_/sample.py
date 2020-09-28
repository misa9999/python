#!/usr/bin/env python3

import os
import sys
import shutil
import fnmatch

from pytube import YouTube
from moviepy.editor import AudioFileClip


def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)


def display_progress_bar(bytes_received, filesize, ch='█', scale=0.55):
    _, columns = get_terminal_size()
    max_width = int(columns * scale)

    filled = int(round(max_width * bytes_received / float(filesize)))
    remaining = max_width - filled
    bar = ch * filled + ' ' * remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = ' ↳ |{bar}| {percent}%\r'.format(bar=bar, percent=percent)
    sys.stdout.write(text)
    sys.stdout.flush()


def on_progress(chunk, file_handle, bytes_remaining):
    audio_filesize
    bytes_received = audio_filesize - bytes_remaining
    display_progress_bar(bytes_received, audio_filesize)


def file_path():  # grabs the file path for Download
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path


def start():

    print('''
    [*] - Download Music
    [*] - Download Video
    [*] - Download Playlist
    [*] - Exit\n''')

    print(f"Your download will be saved to:{file_path()}\n")

    # inputs
    option = input('Enter the option: ')
    yt_url = input("Copy and paste your Youtube URL here: ")
    print('\n')

    if option.lower() == 'music':
        download_music(yt_url)
    elif option.lower() == 'video':
        pass
    elif option.lower() == 'playlist':
        pass
    elif option.lower() == 'exit':
        exit()


def download_music(yt_url):
    print("Acessing Youtube URL...\n")
    # searches for the video and sets up the callback to run the progress bar
    try:
        audio = YouTube(yt_url, on_progress_callback=on_progress)
    except Exception as e:
        print("Error. Check your:\n -connection\n-url is a Youtube url\n\nTry again.")
        prnt(f"Error: {e}")
        # redo = start()

    # get the first audio type - usually the best quality
    audio_type = audio.streams.filter(only_audio=True).first()

    # get the title of the video
    title = audio.title

    # prepares the file for download
    print(f"Fetching: {title}...")
    global audio_filesize
    audio_filesize = audio_type.filesize

    # starts the download process
    audio_type.download(file_path())

    # print("Ready to download another music.\n\n")
    # again = start()
    # path = '/home/yuukiasuna/Desktop/misa/python/scripts/convert/'

    # convert(path)


def download_video(url):
    yt = YouTube(url)

    video = yt.streams.filter(progressive=True).order_by('resolution')\
        .desc().first()
    path = input(f'{yellow}Enter the destination: {reset}/home/yuukiasuna/')
    video.download(f'/home/yuukiasuna/{path}')
    print(f'{yt.title} {green}Has been successfully downloaded.{reset}')


def convert(path):
    for root, folders, files in os.walk(path):
        for file_ in files:
            if not fnmatch.fnmatch(file_, '*.mp4'):
                continue

            complete_path = os.path.join(root, file_)
            filename, file_extension = os.path.splitext(complete_path)

            mp4_file = filename + '.mp4'
            mp3_file = filename + '.mp3'

            if not os.path.isfile(mp4_file):
                continue

            audio = AudioFileClip(mp4_file)
            audio.write_audiofile(mp3_file)
            audio.close()

            os.remove(mp4_file)

            # save_as = input('Save as: /home/yuukiasuna/')
            # destination = f'/home/yuukiasuna/{save_as}/'

            new_filename = mp3_file.split('/')
            destination = '/home/yuukiasuna/Downloads/Music/'
            shutil.move(mp3_file, destination + new_filename[-1])


# begin = start()
if __name__ == "__main__":
    start()

"""
pl = Playlist(PLAYLIST LINK)
pl.download_all()
# or if you want to download in a specific directory
pl.download_all('/path/to/directory/')
"""
