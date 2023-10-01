#!/usr/bin/python3
"""
Defines a Square class, a subclass of Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class  Square that inherits from Rectangle"""
    def __init__(self, size):

        """
        Initialization of a new Square.

        Args:
            size (int): The length of each side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
