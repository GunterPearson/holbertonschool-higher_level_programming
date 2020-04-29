#!/usr/bin/python3
def remove_char_at(str, n):
    strg = ""
    if n >= 0:
        strg + str[:n]
        strg += str[n + 1:]
    else:
        strg = str
    return(strg)
