#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        if ord(str[s]) >= 97 and ord(str[s]) <= 122:
            x = chr(ord(str[s]) - 32)
        else:
            x = str[s]
        print(x, end='')
    print("")
