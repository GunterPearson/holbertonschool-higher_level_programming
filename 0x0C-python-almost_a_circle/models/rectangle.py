#!/usr/bin/python3
"""
create sub class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ sub class of base """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ return width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ return height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set hieght """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ return private x value """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x value """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ return private y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y value """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns area """
        return self.width * self.height

    def display(self):
        """ prints self in # """
        for x in range(self.y):
            print()
        st = " " * self.x
        for x in range(self.height):
            print(st, end="")
            for x in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """ control what gets printed """
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args, **kwargs):
        """ update using *args """
        x = 0
        if args and len(args) != 0:
            l = [self.id, self.width, self.height, self.x, self.y]
            for arg in args:
                if x > 4:
                    break
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
                l[x] = arg
                x += 1
            l = tuple(l)
            self.id, self.width, self.height, self.x, self.y = l
        elif kwargs and len(kwargs) != 0:
            l = ["id", "width", "height", "x", "y"]
            n = [self.id, self.width, self.height, self.x, self.y]
            for key, value in kwargs.items():
                for b in range(len(l)):
                    if b > 4:
                        break
                    if key == l[b]:
                        n[b] = value
            n = tuple(n)
            if l[0] == "id":
                self.__init__(self.width, self.height, self.x, self.y)
            self.id, self.width, self.height, self.x, self.y = n

    def to_dictionary(self):
        """ return dict """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
