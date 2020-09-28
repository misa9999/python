#!/usr/bin/env python3
from pyfiglet import figlet_format
from random import choice, randint
from colored import fg


msg = input("Word: ")
ascii_art = figlet_format(msg)

print(f'{fg(randint(1, 255))} {ascii_art}')