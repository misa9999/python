#!/usr/bin/python
import os
import fnmatch

from moviepy.editor import AudioFileClip

# defaul_path = '/home/yuukiasuna/Downloads/Music/'
origin_path = input('[*] Enter The Path To The Download File: ')
for root, folders, files in os.walk(origin_path):
    for file_ in files:  # file_ = mp4
        if not fnmatch.fnmatch(file_, '*.mp4'):
            continue

        complete_path = os.path.join(root, file_)
        filename, file_extension = os.path.splitext(complete_path)

        mp4_file = filename + '.mp4'
        mp3_file = filename + '.mp3'

        print(mp4_file)
        a = input('saas')

        if not os.path.isfile(mp4_file):
            continue

        audio = AudioFileClip(mp4_file)
        audio.write_audiofile(mp3_file)
        audio.close()
