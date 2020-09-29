"""
class File:
    def __init__(self, file, mode):
        print("opening file")
        self.file = open(file, mode)

    def __enter__(self):
        print("returning file")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing file")
        self.file.close()


with File("abc.txt", "w") as file:
    file.write("zzzzzzzzzzzzz")
"""
from contextlib import contextmanager


@contextmanager
def filee(file, mode):
    try:
        print("Opening file")
        file = open(file, mode)
        yield file
    finally:
        print("Closing file")
        file.close()


with filee("abc.txt", "w") as file:
    file.write("Line 1 \n")
    file.write("Line 2 \n")
    file.write("Line 3 \n")
