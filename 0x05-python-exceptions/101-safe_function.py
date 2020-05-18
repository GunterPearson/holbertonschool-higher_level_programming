#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as exp:
        string = "Exception: " + str(exp) + '\n'
        sys.stderr.write(string)
        return None
