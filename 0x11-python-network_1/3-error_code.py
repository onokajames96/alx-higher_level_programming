#!/usr/bin/python3
"""takes in a URL, sends a request to the URL."""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print('Error code: {}'.format(err.code))
