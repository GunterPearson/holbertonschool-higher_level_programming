#!/usr/bin/python
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            x = ord(s)
            x = x - 32
            s = chr(x)
        print(s, end='')    
    print()    
