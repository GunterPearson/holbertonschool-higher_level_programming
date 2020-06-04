#!/usr/bin/python3
"""
read x number of lines
"""


def read_lines(filename="", nb_lines=0):
    """ reads x number of lines """
    i = 0
    with open(filename, mode="r", encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        else:
            for line in f:
                if i < nb_lines:
                    print(line.rstrip(), end="")
                i += 1
