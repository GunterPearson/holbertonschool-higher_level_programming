#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 != 0:
        x = i - 32
    else:
        x = i
    print(chr(x), end='')
    i -= 1
