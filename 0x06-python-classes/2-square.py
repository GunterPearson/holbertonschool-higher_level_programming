#!/usr/bin/python3
""" Class Square: creates class """


class Square:
    """ creates class with private size """
    def __init__(self, size=0):
        """ check if size is int """
        if isinstance(size, int):
            """ check if size > 0 """
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
