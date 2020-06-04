#!/usr/bin/python3
""" load from json """


def load_from_json_file(filename):
    """ load from json """
    import json
    with open(filename, "r") as f:
        return json.load(f)
