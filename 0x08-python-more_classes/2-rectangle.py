#!/usr/bin/python3
"""
Class Rectangle:
creating new class rectangle
no methods yet
"""


class Rectangle:
    """ Rectangle class """
    @property
    def width(self):
        """ gets private width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets private width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets private height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets private height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """ public setter """
        self.width = width
        self.height = height

    def area(self):
        """ public area """
        return self.width * self.height

    def perimeter(self):
        """ public perim """
        if self.width is 0 or self.height is 0:
            return 0
        return self.width * 2 + self.height * 2
