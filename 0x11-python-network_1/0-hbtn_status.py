#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status."""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
if __name__ == '__main__':
    """Fetches https://alx-intranet.hbtn.io/status using urllib."""
    with urllib.request.urlopen(url) as response:
        body = response.read()
        body_str = body.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body_str))
