#!/usr/bin/python3
"""
create class base
"""


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
            import json
            return json.dumps(list_dictionaries)
