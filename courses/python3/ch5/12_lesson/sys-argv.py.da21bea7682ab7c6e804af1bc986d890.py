#!/usr/bin/env python3

import sys
import os


args = sys.argv
total_args = len(args)

if total_args <= 1:
    print("Missing args:")
    print("-a", "List all files", sep="\t")
    print("-d", "List all directories", sep="\t")
    sys.exit()


so_files = False
so_directories = False

if "-a" in args:
    so_files = True

if "-d" in args:
    so_directories = True

for file in os.listdir("."):
    if so_files:
        if os.path.isfile(file):
            print(file)

    if so_directories:
        if os.path.isdir(file):
            print(file)
