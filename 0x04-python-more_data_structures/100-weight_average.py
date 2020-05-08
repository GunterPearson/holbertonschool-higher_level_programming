#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return 0
    i = 0; j = 0
    for x in my_list:
        i += x[0] * x[1]
        j += x[1]
    i = i / j
    return i
