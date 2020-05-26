#!/usr/bin/python3
"""
Class Rectangle:
creating new class rectangle
no methods yet
"""


class Rectangle:
    """ Rectangle Class """
    @property
    def width(self):
        """ gets private width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets private width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ gets private height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets private height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
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
        if self.height is 0 or self.width is 0:
            return 0
        return self.width * 2 + self.height * 2

    def __str__(self):
        """ control whats printed """
        st = ""
        if self.width is 0 or self.height is 0:
            return st
        for x in range(self.height):
            for y in range(self.width):
                st += "#"
                if y + 1 == self.width and x + 1 != self.height:
                    st += "\n"
        return st

    def __repr__(self):
        """ control repr """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ prints message on delete """
        print("Bye rectangle...")
