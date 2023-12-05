#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    try:
        url = "http://0.0.0.0:5000/search_user"
        data = {'q': q}
        r = requests.post(url, data).json()

        if {'id', 'name'} <= r.keys():
            print('[{id}] {name}'.format(id=r.get('id'), name=r.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
