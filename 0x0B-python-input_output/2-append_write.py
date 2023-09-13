#!/usr/bin/python3
"""
Defination of a function that appends
a string at the end of a text file.
"""

def append_write(filename="", text=""):
    """
    Append a string to a text file (UTF-8)
    and return the number of characters added.

    Args:
        filename (str): The name of the file to which text will be appended.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
