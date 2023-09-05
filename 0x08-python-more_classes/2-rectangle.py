#!/usr/bin/python3

"""Class Rectangle"""

class Rectangle:
    """Defines Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialization.
        Args:
            width(int): the rectangles width.
            height(int):the height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets it"""
         if not isinstance(value, int):
             raise TypeError("width must be an integer")

         if value < 0:
             raise ValueError("width must be >= 0")

         self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    if not isinstance(value, int):
        raise TypeError("height must be an integer")

    if value < 0:
        raise ValueError("height must be >= 0")

    self.__height = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height


    def perimeter(self):
        """The perimetre"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

