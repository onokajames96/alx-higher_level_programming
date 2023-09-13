#!/usr/bin/python3
"""
A file writing function Defined.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8)
    and return the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
