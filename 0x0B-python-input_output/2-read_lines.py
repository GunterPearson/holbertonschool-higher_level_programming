#!/usr/bin/python3
"""
read x number of lines
"""


def read_lines(filename="", nb_lines=0):
    """ reads x number of lines """
    i = 0
    if nb_lines <= 0:
        with open(filename, mode="r", encoding="utf-8") as f:
            print(f.read())
    else:
        with open(filename, mode="r", encoding="utf-8") as f:
            for line in f:
                if i < nb_lines:
                    print(line.rstrip())
                i += 1
