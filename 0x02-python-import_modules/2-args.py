#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    arg_len = len(argv)
    if arg_len == 1:
        print("0 arguments.")
    elif arg_len > 1:
        print("{} arguments:".format(arg_len - 1))
        for x in range(1, arg_len):
            print("{}: {}".format(x, sys.argv[x]))
