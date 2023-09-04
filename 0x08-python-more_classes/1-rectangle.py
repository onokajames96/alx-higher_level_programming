#!/usr/bin/python3


""" """

class Rectangle:

    """Rectangle class defined"""

    def __init__(self, width=0, height=0):

        """Initialization.

        Args:
            width(int): The rectangles width.
            height(int): the Rectangles height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Getter for width, to get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width, to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value


    @property
    def height(self):
        """Getter for height, to get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height, to set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
