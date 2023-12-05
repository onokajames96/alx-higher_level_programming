#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Prints an error message if the HTTP status
code is greater than or equal to 400.
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])

    if r.status_code >= 400:
        print('Error code:', r.status_code)
    else:
        print(r.text)
