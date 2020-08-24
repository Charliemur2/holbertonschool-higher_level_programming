#!/usr/bin/python3
"""
script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header with requests lib
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    header = r.headers
    print(header.get('X-Request-Id'))
