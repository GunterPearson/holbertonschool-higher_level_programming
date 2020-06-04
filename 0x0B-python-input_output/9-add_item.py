#!/usr/bin/python3
""" add item """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    l = load_from_json_file("add_item.json")
except:
    l = []
for i in range(1, len(sys.argv)):
    l.append(sys.argv[i])
save_to_json_file(l, "add_item.json")
