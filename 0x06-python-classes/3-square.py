#!/usr/bin/python3
"""a class Square that defines a square"""

class Square():
    """ Square.
    """
    def __init__(self, size=0):
        """Initialization.
        Args:
            size(int): The Size of square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """ that returns the current square area.
        """
        return (self.__size * self.__size)
