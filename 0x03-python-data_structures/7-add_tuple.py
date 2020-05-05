#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        tuple_a = (0, 0)
    if tuple_b == ():
        tuple_b = (0, 0)
    list_a = list(tuple_a)
    if len(list_a) < 2:
        list_a.append(0)
    list_b = list(tuple_b)
    if len(list_b) < 2:
        list_b.append(0)
    final = [list_a[0] + list_b[0], list_a[1] + list_b[1]]
    ret = tuple(final)
    return ret
