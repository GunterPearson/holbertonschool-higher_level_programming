#!/usr/bin/python3
""" Class Sqaure: creating class square """


class Square:
    """ set private int size """
    def __init__(self, size=0):
        """ check if value is int """
        if isinstance(size, int):
            """ check size is >= 0 """
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    """ return area of square """
    def area(self):
        """ square size given """
        return self.__size ** 2
