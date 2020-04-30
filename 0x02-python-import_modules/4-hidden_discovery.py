#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import re
    a = ["", ""]
    a = dir(hidden_4)
    for x in range(len(a)):
        if a[x][:2] == '__':
            continue
        print(a[x])
