#!/usr/bin/python3
""" error code"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    requests = urllib.request.Request(url)
    with urllib.request.urlopen(requests) as html:
        print(html.read().decode("utf-8"))
