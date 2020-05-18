#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    i = 0
    try:
        a, b = args
        i = fct(a, b)
        return i
    except Exception as exp:
        string = "Exception: " + str(exp) + '\n'
        sys.stderr.write(string)
        return None
