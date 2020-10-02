import os
import subprocess
import fnmatch


PATH = "/home/anthrax/git/python/scripts/testing"


def convert(path):
    list_files = []
    ext = input("Search extension: ")
    for root, folders, files in os.walk(path):
        for file in files:
            if not fnmatch.fnmatch(file, "*" + ext):
                continue

            list_files.append(file)

        all_files = len(list_files)
        for index, file in enumerate(list_files):
            print(f"[{index}] - {file}")

        print(f"[{all_files}] - all")

        opt = int(input("Choose one file or all: "))

        if opt == all_files:
            exit()

        complete_path = os.path.join(root, list_files[opt])
        filename, file_extension = os.path.splitext(complete_path)

        output_file = input("Enter output file: ")

        fullname_ext1 = filename + file_extension
        fullname_ext2 = filename + "." + output_file

        try:
            subprocess.call(
                [
                    "ffmpeg",
                    "-i",
                    os.path.join(path, fullname_ext1),
                    os.path.join(path, fullname_ext2),
                    "-v",
                    "-8",
                ]
            )
        except Exception as error:
            print(error)


convert(PATH)
