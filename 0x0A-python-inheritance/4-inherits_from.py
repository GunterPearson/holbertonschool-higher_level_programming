#!/usr/bin/python3
"""
inherits_from
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
