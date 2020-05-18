#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            y += 1
            if y == x:
                print()
        except:
            print()
            return y
    return y
