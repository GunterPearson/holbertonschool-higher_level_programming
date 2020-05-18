#!/usr/bin/python3
def safe_print_division(a, b):
    quot = 0
    try:
        quot = a / b
    except:
        quot = None
    finally:
        print("Inside Result: {}".format(quot))
        return quot
