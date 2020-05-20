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
        if len(value) != 2:
            raise TypeError(str)
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError(str)
        if value[0] < 0 or value[1] < 0:
            raise TypeError(str)
        else:
            self.__position = value

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
            for y in range(self.position[1]):
                print()
            for x in range(self.size):
                for z in range(self.position[0] + self.size):
                    if z < self.position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print()
