#!/usr/bin/python3
""" Class Square: set class """


class Square:
    """ gets size """
    @property
    def size(self):
        return self.__size

    """ sets size """
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

    """ gets position """
    @property
    def position(self):
        return self.__position

    """ sets postion """
    @position.setter
    def position(self, value):
        str = "position must be a tuple of 2 positive integers"
        if type(value) is tuple:
            if value[0] >= 0 and value[1] >= 0:
                self.__position = value
            else:
                raise TypeError(str)

    """ init function sets public value """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ return squared size """
    def area(self):
        return self.size ** 2

    """ prints square """
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for x in range(self.size):
                if self.position:
                    for z in range(self.position[0]):
                        print(" ", end="")
                for y in range(self.size):
                    print("#", end="")
                print()
