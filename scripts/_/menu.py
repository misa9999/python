import os
import sys

from pytube import YouTube


def get_terminal_size():
    """Return the terminal size in rows and columns."""
    rows, columns = os.popen('stty size', 'r').read().split()
    return int(rows), int(columns)


def display_progress_bar(bytes_received, filesize, ch='█', scale=0.55):
    """Display a simple, pretty progress bar.
    Example:
    ~~~~~~~~
    PSY - GANGNAM STYLE(강남스타일) MV.mp4
    ↳ |███████████████████████████████████████| 100.0%
    :param int bytes_received:
        The delta between the total file size (bytes) and bytes already
        written to disk.
    :param int filesize:
        File size of the media stream in bytes.
    :param ch str:
        Character to use for presenting progress segment.
    :param float scale:
        Scale multipler to reduce progress bar size.
    """
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
    global filesize
    bytes_received = filesize - bytes_remaining
    display_progress_bar(bytes_received, filesize)


url = 'https://www.youtube.com/watch?v=tQblSS2kl4Q'
yt = YouTube(str(url), on_progress_callback=on_progress)

info = yt.streams.filter(progressive=True).order_by('resolution').desc()\
    .first()

filesize = info.filesize
info.download()
