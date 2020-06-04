#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """Reading file"""
    with open(filename, encoding='utf-8') as files:
        print(files.read())
