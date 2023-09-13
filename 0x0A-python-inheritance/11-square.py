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
        super().__init__(size, size)
        self.__size = size
