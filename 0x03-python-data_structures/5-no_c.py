#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    else:
        new_string = list(my_string)
        try:
            new_string.remove('c')
        except:
            pass
        try:
            new_string.remove('C')
        except:
            pass
        return ''.join(new_string)
