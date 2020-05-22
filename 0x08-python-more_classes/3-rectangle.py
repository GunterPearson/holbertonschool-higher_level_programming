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

    """ public area """
    def area(self):
        return self.width * self.height

    """ public perim """
    def perimeter(self):
        if self.height is 0 or self.width is 0:
            return 0
        return self.width * 2 + self.height * 2

    """ control whats printed """
    def __str__(self):
        st = ""
        if self.width is 0 or self.height is 0:
            return st
        for x in range(self.height):
            for y in range(self.width):
                st += "#"
                if y + 1 == self.width and x + 1 != self.height:
                    st += "\n"
        return st
