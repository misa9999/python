from zipfile import ZipFile
import os

path = r"/home/anthrax/git/python/courses/python3/ch5/11_lesson/files/"
with ZipFile("file.zip", "w") as zip:
    for file in os.listdir(path):
        complete_path = os.path.join(path, file)
        zip.write(complete_path, file)


with ZipFile("file.zip", "r") as zip:
    for file in zip.namelist():
        print(file)


with ZipFile('file.zip', 'r') as zip:
    zip.extractall('unzipped')
