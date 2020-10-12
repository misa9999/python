import os
import shutil

videos_ext = [".mp4", ".mkv", ".avi"]
docs_ext = [".txt", ".pdf"]
images_ext = [".jpeg", ".png", ".jpg"]
audios_ext = [".mp3", ".wav"]

home = os.path.expanduser("~")
origin_path = home + "/Documents/os_examples"


def get_extension(name):
    index = name.rfind(".")
    return name[index:]


def organize(directory):
    AUDIOS_DIR = os.path.join(directory, "audios")
    IMAGES_DIR = os.path.join(directory, "images")
    DOCS_DIR = os.path.join(directory, "documents")
    VIDEOS_DIR = os.path.join(directory, "videos")
    OTHERS_DIR = os.path.join(directory, "others")

    if not os.path.isdir(AUDIOS_DIR):
        os.mkdir(AUDIOS_DIR)
    if not os.path.isdir(IMAGES_DIR):
        os.mkdir(IMAGES_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(OTHERS_DIR):
        os.mkdir(OTHERS_DIR)


    filenames = os.listdir(directory)
    new_folder = ' '
    for file in filenames:
        if os.path.isfile(os.path.join(directory, file)):
            extension = str.lower(get_extension(file))
            print(f"File: '{file}' -> Ext: {extension}")

            if extension in audios_ext:
                new_folder = AUDIOS_DIR
            elif extension in videos_ext:
                new_folder = VIDEOS_DIR
            elif extension in images_ext:
                new_folder = IMAGES_DIR
            elif extension in docs_ext:
                new_folder = DOCS_DIR
            else:
                new_folder = OTHERS_DIR

            old = os.path.join(directory, file)
            new = os.path.join(new_folder, file)
            os.rename(old, new)
            print(f"Moved {old} -> {new}")


if __name__ == "__main__":
    organize(origin_path)
