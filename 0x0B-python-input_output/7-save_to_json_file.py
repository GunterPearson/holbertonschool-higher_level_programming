#!/usr/bin/python3
""" save to json """


def save_to_json_file(my_obj, filename):
    """ save to json """
    import json
    with open(filename, "w") as f:
        json.dump(my_obj, f)
