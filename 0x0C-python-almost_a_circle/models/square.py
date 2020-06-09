#!/usr/bin/python3
"""
square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ sub class of rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ init with super """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ control what gets printed """
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width)

    @property
    def size(self):
        """ return size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update square """
        x = 0
        if args and len(args) != 0:
            l = [self.id, self.size, self.x, self.y]
            for arg in args:
                if x > 3:
                    break
                if arg is None:
                    self.__init__(self.size, self.x, self.y)
                else:
                    self.id = arg
                l[x] = arg
                x += 1
            l = tuple(l)
            self.id, self.size, self.x, self.y = l
        elif kwargs and len(kwargs) != 0:
            l = ["id", "size", "x", "y"]
            n = [self.id, self.size, self.x, self.y]
            for key, value in kwargs.items():
                for b in range(len(l)):
                    if b > 3:
                        break
                    if key == l[b]:
                        n[b] = value
            n = tuple(n)
            if l[0] == "id":
                self.__init__(self.width, self.height, self.x, self.y)
            self.id, self.size, self.x, self.y = n

    def to_dictionary(self):
        """ prints dict """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
