#!/usr/bin/python3
"""
4-print_square module
contains function
print_square
"""


def print_square(size):
    """
    print square based on size
    """
    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [[print("#", end="") if y + 1 < size else print("#")
        for y in range(size)] for x in range(size)]
