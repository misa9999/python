import os
import subprocess
import fnmatch


class Convert:
    def __init__(self):
        self.path = ""
        self.list_files = []

    def file_path(self):
        print("[ 1 ]  - Downloads")
        print("[ 2 ]  - Downloads/Music")
        print("[ 3 ]  - Downloads/Video")
        print("[ 4 ]  - Videos")
        print("[ 5 ]  - Music")
        print("[ 6 ]  - Custom path")
        print("[ 7 ]  - Exit")

        opt = int(input("Choose one: "))

        home = os.path.expanduser("~")
        download_path = os.path.join(home, "Downloads")
        download_path_music = os.path.join(home, "Downloads/Music")
        download_path_video = os.path.join(home, "Downloads/Video")
        video_path = os.path.join(home, "Videos")
        music_path = os.path.join(home, "Music")
        custom_path = os.path.join(home, "")

        if opt == 1:
            self.path = download_path
        elif opt == 2:
            self.path = download_path_music
        elif opt == 3:
            self.path = download_path_video
        elif opt == 4:
            self.path = video_path
        elif opt == 5:
            self.path = music_path
        elif opt == 6:
            custom = input("Custom path: ")
            self.path = custom_path + custom
        elif opt == 7:
            exit()

    def search(self):
        extension = input("Search extensions: ")
        self.file_path()
        for root, folders, files in os.walk(self.path):
            for file in files:
                if not fnmatch.fnmatch(file, "*" + extension):
                    continue

                self.list_files.append(file)

            self.list_items(root)

    def list_items(self, root):
        exit_prog = len(self.list_files)
        for index, file in enumerate(self.list_files):
            print(f"[{index}] - {file}")

        print(f"[{exit_prog}] - Exit")
        opt = int(input("Choose one file or all: "))

        if opt == exit_prog:
            exit()

        complete_path = os.path.join(root, self.list_files[opt])
        filename, file_extension = os.path.splitext(complete_path)

        output_file = input("Enter output file: ")

        fullname_ext1 = filename + file_extension
        fullname_ext2 = filename + "." + output_file

        self.convert(fullname_ext1, fullname_ext2)

    def convert(self, ext1, ext2):
        try:
            subprocess.call(
                [
                    "ffmpeg",
                    "-i",
                    os.path.join(self.path, ext1),
                    os.path.join(self.path, ext2),
                ]
            )
        except Exception as error:
            print(error)


file = Convert()
file.search()
