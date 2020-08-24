#!/usr/bin/python3
""" 7-error"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
    except:
        print("Error code: {}".format(r.status_code))
