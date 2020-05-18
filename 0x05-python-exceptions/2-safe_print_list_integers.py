#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
    i = 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            i += 1
            y += 1
        except:
            y += 1
            pass
    print()
    return i
