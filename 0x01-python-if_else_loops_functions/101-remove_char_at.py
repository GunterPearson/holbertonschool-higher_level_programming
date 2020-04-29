#!/usr/bin/python3
def remove_char_at(str, n):
    if n <= 0:
        return(str)
    else:
        strg = str[:n]
        strg += str[n + 1:]
    return(strg)
