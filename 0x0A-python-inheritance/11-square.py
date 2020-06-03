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

    def area(self):
        """ return area """
        return self.__height * self.__width

    def __str__(self):
        """ control print """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

"""
Square class
"""


class Square(Rectangle):
    """ square sub class """
    def __init__(self, size):
        """ set public size """
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """ control print """
        return "[Square] {}/{}".format(self.__size, self.__size)
