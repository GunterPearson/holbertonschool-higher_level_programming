#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """Reading file"""
    with open(filename, mode="r", encoding='UTF8') as files:
        print(files.read(), end="")
