#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as stn:
        string = "Exception: " + str(stn) + '\n'
        sys.stderr.write(string)
        return False
