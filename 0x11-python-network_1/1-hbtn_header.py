#!/usr/bin/python3
"""
Fetches the value of the X-Request-Id variable from the header of the response.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
