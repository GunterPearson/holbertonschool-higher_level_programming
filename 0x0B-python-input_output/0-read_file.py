#!/usr/bin/python3
"""read text file and prints to stdout"""


def read_file(filename=""):
    """reads text file"""
    with open(filename) as f:
        print(f.read(), end="")
