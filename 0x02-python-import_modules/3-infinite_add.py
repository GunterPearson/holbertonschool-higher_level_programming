#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if len(argv) == 1:
        print('0')
    elif len(argv) == 2:
        print("{}".format(int(argv[1])))
    elif len(argv) > 2:
        i = 0
        for x in range(1, len(argv)):
            i += int(argv[x])
        print(i)
