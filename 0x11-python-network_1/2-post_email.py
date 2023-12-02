#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email.
"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    data = urlencode({
                        'email': argv[2]
                    }).encode('ascii')
    request = Request(argv[1], data)

    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
