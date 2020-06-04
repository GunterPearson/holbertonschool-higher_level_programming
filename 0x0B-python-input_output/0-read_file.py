#!/usr/bin/python3
"""
Reading Files
"""


def read_file(filename=""):
    """ reads a file """
    with open(filename, encoding='UTF8') as file:
        print(file.read())
