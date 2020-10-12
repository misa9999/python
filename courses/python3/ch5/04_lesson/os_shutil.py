import os
import shutil

home = os.path.expanduser("~")
origin_path = home + "/Documents/os_examples"
new_path = home + "/Documents/os_examples2"

try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(f"cannot create directory '{new_path}' File exists")


for root, dirs, files in os.walk(origin_path):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)

        if ".mp4" in file:
            shutil.copy(old_file_path, new_file_path)
            print(f"File: {file} moved")
