#!/usr/bin/python3
"""
BaseGeometry
"""


class BaseGeometry:
    """ geometry class """
    def area(self):
        """ raises exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
Rectangle class
"""


class Rectangle(BaseGeometry):
    """ Rectangle class """
    def __init__(self, width, height):
        """ instant of width and height"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)
