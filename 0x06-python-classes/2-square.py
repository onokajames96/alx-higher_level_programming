#!/usr/bin/python3
""" defination of square.
"""


class Square:
    """ class Square that defines a square.
    """

    def __init__(self, size=0):
        """ Initialization.

        Args:
            size (int): The Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
