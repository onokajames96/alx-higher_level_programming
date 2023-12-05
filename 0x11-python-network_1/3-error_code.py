#!/usr/bin/python3
"""takes in a URL, sends a request to the URL."""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
