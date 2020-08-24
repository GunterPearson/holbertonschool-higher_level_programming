#!/usr/bin/python3
""" email post"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    requests = urllib.request.Request(url, data)
    with urllib.request.urlopen(requests) as html:
        print(html)
