#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        my_list.sort()
        l = len(my_list) - 1
        return my_list[l]
