#!/usr/bin/python3

"""A Class Square defines a square.
"""

class Square:
    """ Object Square.
    """
    def __init__(self, size=0):
        """ Instantiation.
        Args:
            
            size(int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Retrieves it."""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets it.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        """That returns the current square area.
        """

        return self.__size * self.__size
