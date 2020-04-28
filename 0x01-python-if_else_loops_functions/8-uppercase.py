#!/usr/bin/python3
def uppercase(str):
    for s in range(len(str)):
        c = ord(str[s]) - 32
        print("{}".format(chr(c)) if ord(str[s]) >= 97 and ord(
            str[s]) <= 122 else "{}".format(str[s]), end='')
    print("")
