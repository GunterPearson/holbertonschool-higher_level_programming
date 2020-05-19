#!/usr/bin/python3
""" Class Square: set class """


class Square:
    """ get the size """
    @property
    def size(self):
        """ return size """
        return self.__size

    """ set private size """
    @size.setter
    def size(self, value):
        """ check to see if size is int """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    """ set normal size """
    def __init__(self, size=0):
        """ initalize size """
        self.size = size

    """ return area of square """
    def area(self):
        """ multiply and return """
        return self.size ** 2

    """ prints squre in # """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                for y in range(self.size):
                    print("#", end="")
                print()
