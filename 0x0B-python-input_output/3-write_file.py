#!/usr/bin/python3
"""
write to file
"""


def write_file(filename="", text=""):
    """ writes to file """
    with open(filename, mode="w", encoding="utf-8") as f:
        num = f.write(text)
    return (num)
