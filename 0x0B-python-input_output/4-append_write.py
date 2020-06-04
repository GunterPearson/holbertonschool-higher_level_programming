#!/usr/bin/python3
""" Append to a file"""


def append_write(filename="", text=""):
    """ appends text"""
    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
    return len(text)
