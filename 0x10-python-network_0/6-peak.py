#!/usr/bin/python3
""" finds peak """


def find_peak(list_of_integers):
    """ finds peak of integers"""
    if list_of_integers == []:
        return None
    new = 0
    for x in range(len(list_of_integers)):
        if x > 0:
            if list_of_integers[x - 1] < list_of_integers[x]:
                if list_of_integers[x] > list_of_integers[new]:
                    new = x
    return list_of_integers[new]
