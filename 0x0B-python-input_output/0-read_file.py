#!/usr/bin/python3
"""
A function that reads a Text file.
"""


def read_file(filename=""):
    """
    Read and print the content of a text file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
