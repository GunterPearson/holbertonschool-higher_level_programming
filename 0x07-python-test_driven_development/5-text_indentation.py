#!/usr/bin/python3
"""
5-text_indentation
files in module:
text_indentation
"""


def text_indentation(text):
    """
    indents text
    """
    check = 0
    if type(text) is not str or text is None:
        raise TypeError("text must be a string")
    for c in text:
        if c is '.' or c is ':' or c is '?':
            check = 1
            print(c, end="")
            print()
            print()
        else:
            if check is 1:
                check = 0
                if c is ' ' or c is '\t':
                    continue
            else:
                print(c, end="")
