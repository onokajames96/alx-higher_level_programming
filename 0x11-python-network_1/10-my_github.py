#!/usr/bin/python3
"""takes  GitHub credentials
uses the GitHub API to display your id."""
import requests
from sys import argv


if __name__ == "__main__":
    auth = (argv[1], argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
