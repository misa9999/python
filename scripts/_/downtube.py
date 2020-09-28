#!/usr/bin/env python3
import os
from time import sleep

from colored import fg, attr


# colors
colors = {
    'yellow': fg(226),
    'green': fg(82),
    'red': fg(196),
    'pink': fg(198),
    'orange': fg(208),
    'cyan': fg(122),
    'violet': fg(128),
}

reset = attr('reset')
yellow = colors['yellow']
red = colors['red']
green = colors['green']
pink = colors['pink']
orange = colors['orange']
cyan = colors['cyan']
violet = colors['violet']


class Download:
    def menu(self):
        print()
        print(
            f"{violet}[ 1 ] - Download Music{ reset}\n"
            f"{violet}[ 2 ] - Download Video{ reset}\n"
            f"{violet}[ 3 ] - Exit{ reset}\n"
        )

        print()
        option = int(input('Option: '))

        if option == 1:
            ydl.down_music()
        elif option == 2:
            ydl.down_video()
        elif option == 3:
            exit()
        else:
            print(f'{red}error{reset}')

    def down_music(self):
        url = input(f'{green}Please enter the Youtube Video URL: {reset}')

        print('\n', flush=True)
        sleep(0.045)

        video_info = input(f'{yellow}Download one song or playlist? {reset}')

        print('\n', flush=True)
        sleep(0.045)

        if video_info.lower() == 'one':
            # path = input('Type path: ')
            music_info = 'youtube-dl -x --audio-format mp3'
            path = "~/Downloads/Music/"
            filename = f'{music_info} -o "{path}%(title)s.%(ext)s" {url}'

            print('\n', flush=True)
            sleep(0.045)

            os.system(filename)

        elif video_info.lower() == 'playlist':
            index = input(f'{red}Index playlist yes/no? {reset}')

            print('\n', flush=True)
            sleep(0.045)

            if index == 'yes':
                start = int(input(f'{green}Start playlist in: {reset}'))
                end = int(input(f'{red}End playlist in: {reset}'))

                print('\n', flush=True)
                sleep(0.045)

                st = f'--playlist-start {start}'
                ed = f'--playlist-end {end}'

                music_info = 'youtube-dl -x --audio-format mp3'
                path = "~/Downloads/Music/"

                filename = f'{music_info} {st} {ed} -o "{path}%(title)s.%(ext)s" {url}'

                print('\n', flush=True)
                sleep(0.045)

                os.system(filename)
            elif index == 'no':
                music_info = 'youtube-dl -x --audio-format mp3'
                path = "~/Downloads/Music/"

                filename = f'{music_info} -o "{path}%(title)s.%(ext)s" {url}'

                os.system(filename)
            else:
                print('ERROR! try again')
        else:
            print('error, try again')

    def down_video(self):
        pass
        # url = input('Please enter the Youtube Video URL: ')

        # video_info = input('Show video info? y/n ')

        # try:
        #     if video_info.lower() in 'y':
        #         os.system(f'youtube-dl -F {url}')
        #         opt = int(input('Choose one format: '))

        #         os.system(f'youtube-dl -f {opt} {url}')
        #     elif video_info.lower() in 'n':
        #         print('will download the best available quality video.', flush=True)
        #         sleep(0.045)
        #         os.system(f'youtube-dl {url}')
        # except Exception as e:
        #     print(f'error: {e}')


ydl = Download()
ydl.menu()


# # url = input('Please enter the Youtube Video URL: ')
# # os.system(f'youtube-dl {url}')
