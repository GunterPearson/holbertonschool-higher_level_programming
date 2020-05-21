#!/usr/bin/python3
"""
Say_my_name module
contains function:
say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    print out first and last name in sentence
    """
    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
