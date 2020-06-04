#!/usr/bin/python3
"""
Reading Files
"""


def read_file(filename=""):
    """ reads a file """
    with open(filename, mode="r", encoding='utf-8') as file:
        print(file.read(), end="")
