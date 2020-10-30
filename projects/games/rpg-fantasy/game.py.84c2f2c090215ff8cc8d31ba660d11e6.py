# python text rpg
# waifu fantasy

import cmd
import textwrap
import sys
import os
import time
import random


from world_map import WorldMap


screen_width = 100

### player setup ###
class Player:
    def __init__(self):
        self.name = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "start"


myPlayer = Player()

### title screen ###
def title_screen_selectons():
    while True:
        option = input("> ")

        if option.lower() == "play":
            start_game()  # placeholder until written
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            break
        else:
            print("Please enter a valid command.")


def title_screen():
    os.system("clear")
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("         - Play -           ")
    print("         - Help -           ")
    print("         - Quit -           ")

    title_screen_selectons()


def help_menu():
    print("############################")
    print("# Welcome to the Text RPG! #")
    print("############################")
    print("- Use, up, down, left, right to move")
    print("- Type your commands to do them")
    print("- Use 'look' to inspect something")
    print("- Good luck and have fun!")


#### GAME INTERACTIVITY ####
def print_location():
    print(f'{"#" * (4 + len(myPlayer.location))}')
    print(f"# {myPlayer.location.upper()} #")
    print(f'# {zonemap["a1"][areas.DESCRIPTION]} #')
    print(f'{"#" * (4 + len(myPlayer.location))}')


def prompt():
    print("\n" + "=================================")
    print("What would you like to do?")

    acceptable_actions = [
        "move",
        "go",
        "travel",
        "walk",
        "quit",
        "examine",
        "inspect",
        "interact",
        "look",
    ]

    while True:
        action = input("> ")

        if action not in acceptable_actions:
            continue

        if action.lower() == "quit":
            break
        elif action.lower() in acceptable_actions[:4]:
            player_move(action.lower())
        elif action.lower() in acceptable_actions[5:]:
            player_examine(action.lower())


def player_move(action):
    ask = "where would you like to move to?\n"
    dest = input(ask)

    if dest == ["up", "north"]:
        destination = zonemap["a1"][areas.UP]
        movement_handler(destination)
    elif dest == ["left", "west"]:
        destination = zonemap["a1"][areas.LEFT]
        movement_handler(destination)
    elif dest == ["right", "east"]:
        destination = zonemap["a1"][areas.RIGHT]
        movement_handler(destination)
    elif dest == ["down", "south"]:
        destination = zonemap["a1"][areas.DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print(f"You have moved to {destination}")
    myPlayer.location = destination
    print_location()


def player_examine(myAction):
    pass


### GAME FUNCTIONALITY ###
def start_game():
    pass


areas = WorldMap()
zonemap = areas.zonemaps()

prompt()
# print(areas.zonemaps())
