#!/usr/bin/python3
""" Class Square: create class square with size and method """


class Square:
    """ creates private attribute size """
    def __init__(self, size):
        """ sets size """
        Square.__size = size
