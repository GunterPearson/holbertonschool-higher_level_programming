#!/usr/bin/python3
"""
my_list
"""


class MyList(list):
    """ sub class of list """
    def print_sorted(self):
        """ public instance of sorted list """
        new = self[:]
        new.sort()
        print(new)
