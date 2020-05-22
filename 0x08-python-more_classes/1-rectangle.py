#!/usr/bin/python3
"""
Class Rectangle:
creating new class rectangle
no methods yet
"""


class Rectangle:
    """ gets private width """
    @property
    def width(self):
        return self.__width

    """ sets private width """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """ gets private height """
    @property
    def height(self):
        return self.__height

    """ sets private height """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """ public setter """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
