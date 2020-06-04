#!/usr/bin/python3
"""
counting lines
"""


def number_of_lines(filename=""):
    """ return number of lines"""
    len = 0
    with open(filename, mode="r", encoding="utf-8") as new:
        for line in new:
            len += 1
        return len
