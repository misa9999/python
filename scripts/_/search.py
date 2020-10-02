#!/user/bin/env python3
import json
import os
import fnmatch

titles = [] # videos title
downloaded = []
to_download = []

def search_file(filename):
	file = open(filename, 'r')

	for line in file.readlines():
		titles.append(line.strip())


def search_in_path(path):
	for root, folders, files in os.walk(path):
		for file_ in files:
			if not fnmatch.fnmatch(file_, '*.mp3'):
				continue

			complete_path = os.path.join(root, file_)
			filename, file_extension = os.path.splitext(complete_path)


			temp = filename.split('/')

			mp3_file = temp[-1]

			downloaded.append(mp3_file)


def get_missing_names():
	for name in range(len(titles)):
		if titles[name] not in downloaded:
			to_download.append(titles[name])

	for missing_name in to_download:
		print(missing_name)


search_file('videos_title.txt')
search_in_path('/home/yuukiasuna/Videos/Antraz/')
get_missing_names()
