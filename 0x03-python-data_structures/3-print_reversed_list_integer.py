#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == []:
        return None
    if len(my_list) == 1:
        print my_list
        return None
    else:
        my_list.reverse()
        for x in range(len(my_list)):
            print("{:d}".format(my_list[x]))
