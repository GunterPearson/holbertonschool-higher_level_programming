#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == "" or roman_string is None:
        return 0
    i = 0
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    list_a = list(roman_string)
    for x in list_a:
        for key in roman_dict.keys():
            if key == x:
                i += roman_dict[key]
    return i
