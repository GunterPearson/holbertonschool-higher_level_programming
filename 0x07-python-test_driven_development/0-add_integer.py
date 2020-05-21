#!/usr/bin/python3
"""
    0-add_integer module:
    add_integer:
    takes float or int and returns addition
"""


def add_integer(a, b=98):
    """
    add int or float a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a + b)
