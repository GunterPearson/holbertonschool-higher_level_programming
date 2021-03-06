#!/usr/bin/python3
"""
create class base
"""
import json


class Base:
    """ privat object """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converts to json """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                d = [x.to_dictionary() for x in list_objs]
                f.write(Base.to_json_string(d))

    @staticmethod
    def from_json_string(json_string):
        """ converts from json """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create method """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances: """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                o = cls.from_json_string(file.read())
                return [cls.create(**x) for x in o]
        except:
            return []
