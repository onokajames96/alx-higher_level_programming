#!/usr/bin/python3
"""takes in a URL, sends a request to the URL."""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
