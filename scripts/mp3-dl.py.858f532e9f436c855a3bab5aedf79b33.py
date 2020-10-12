import os
import sys
import subprocess
import fnmatch

from colored import fg, attr
from pytube import YouTube


red = fg(1)
green = fg(2)
yellow = fg(11)
reset = attr('reset')


def get_terminal_size():
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)

# '█'1


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


def start():  # show menu options
    yt_dl = '''
               __  __ ____ _____       ____  _
	      |  \/  |  _ \___ /      |  _ \| |
	      | |\/| | |_) ||_ \ _____| | | | |
	      | |  | |  __/___) |_____| |_| | |___
	      |_|  |_|_|  |____/      |____/|_____|
    '''
    print(yt_dl)
    print('[1] Download Music')
    print('[2] Download Playlist')
    print('[3] Exit')

    # print(f"Your download will be saved to:{file_path()}\n")

    # inputs
    print()
    option = int(input(f"{yellow}[*] Enter The Option: {reset}"))
    if option == 1:
        download_music(enter_url())
    elif option == 2:
        pass
    elif option == 3:
        exit()


def download_music(yt_url):
    print()
    print(f"{green}[+] Acessing Youtube URL...{reset}\n")
    # searches for the video and sets up the callback to run the progress bar
    try:
        audio = YouTube(yt_url, on_progress_callback=on_progress)
    except Exception as e:
        print(f"{red}Error. Check your:\n \
            -connection\n-url is a Youtube url\n\nTry again.{reset}")
        print(f"Error: {e}")

    # get the first audio type - usually the best quality
    audio_type = audio.streams.filter(only_audio=True).first()

    # get the title of the video
    title = audio.title

    # prepares the file for download
    print(f"{green}[+] Fetching: {reset}{title}...")
    global audio_filesize
    audio_filesize = audio_type.filesize

    # starts the download process
    audio_type.download(file_path())

    print()
    print(f'{green}[+] {reset}{title} \
        {green}Has Been Successfully Downloaded.{reset}')
    convert(file_path())


def convert(path):  # convert mp4 to mp3 using ffmpeg
    print(f'{green}[+] Converting...{reset}')
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

            try:
                subprocess.call([
                    'ffmpeg',
                    '-i', os.path.join(path, mp4_file),
                    os.path.join(path, mp3_file),
                    '-v',
                    '-8'
                ])
            except Exception as error:
                print(f'{red}[!!] Error: {reset}{error}')
            else:
                delete_file = input(f'{red}\
                    [!!] Delete original file?{reset} Y/n ')
                if delete_file in 'yY':
                    os.remove(mp4_file)


def file_path():  # grabs the file path for Download
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads/Music')
    return download_path


def enter_url():
    url = input(f"{yellow}[*] Copy And Paste Your Youtube URL Here: {reset}")
    return url


if __name__ == "__main__":
    start()

"""
pl = Playlist(PLAYLIST LINK)
pl.download_all()
# or if you want to download in a specific directory
pl.download_all('/path/to/directory/')



msg = input("Word: ")
ascii_art = figlet_format(msg)

print(f'{fg(randint(1, 255))} {ascii_art}')
"""
