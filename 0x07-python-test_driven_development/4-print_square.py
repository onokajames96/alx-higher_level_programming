#!/usr/bin/python3

"""module print_square"""

def print_square(size):
    """ a function that prints a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("{}".format('#' * size))

