class Author:
    def __init__(self, name):
        self.__name = name
        self.__tool = None

    @property
    def name(self):
        return self.__name

    @property
    def tool(self):
        return self.__tool

    @tool.setter
    def tool(self, tool):
        self.__tool = tool


class Pen:
    def __init__(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    def write(self):
        print('Pen is writing...')


class TypeWriter:
    def write(self):
        print('Typewriter is writing...')


author = Author('Misa')
pen = Pen('BIC')
tw = TypeWriter()

author.tool = tw
author.tool.write()
