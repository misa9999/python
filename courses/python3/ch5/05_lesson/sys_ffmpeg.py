"""
ffmpeg -i "INPUT" -i "SUBTITLE" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:s srt -map v:0 -map a -map 1:0 
-ss 00:00:00 -to 00:00:10 "OUTPUT"
"""

import os
import fnmatch
import sys


if sys.platform == "linux":
    command_ffmpeg = "ffmpeg"
else:
    command_ffmpeg = r"ffmpeg\ffmpeg.exe"


codec_video = "-c:v libx264"
crf = "-crf 23"
preset = "-preset ultrafast"
codec_audio = "-c:a aac"
bitrate_audio = "-b:a 320k"
debug = "-ss 00:00:00 -to 00:00:10"

origin_path = "/home/anthrax/Documents/input"
destination_path = "/home/anthrax/Documents/output"

for root, folders, files in os.walk(origin_path):
    for file in files:
        if not fnmatch.fnmatch(file, "*.mp4"):
            continue

        complete_path = os.path.join(root, file)
        filename, file_extension = os.path.splitext(complete_path)
        subtitle_path = filename = ".srt"

        if os.path.isfile(subtitle_path):
            input_subtitle = f'-i "{subtitle_path}"'
            map_subtitle = f"-c:s -map v:0 -map a -map 1:0"
        else:
            input_subtitle = ""
            map_subtitle = ""

        filename, file_extension = os.path.splitext(file)

        output_file = f"{destination_path}/{filename}_NEW{file_extension}"

        command = (
            f'{command_ffmpeg} -i "{complete_path}" {input_subtitle} '
            f"{codec_video} {crf} {preset} {codec_video} {bitrate_audio} "
            f'{debug} {map_subtitle} "{output_file}"'
        )

        os.system(command)
