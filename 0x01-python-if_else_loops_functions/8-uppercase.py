#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            x = chr(ord(s) - 32)
        else:
            x = s    
        print(x, end='')
    print("")
