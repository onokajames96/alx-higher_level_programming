#!/usr/bin/python3

"""Class Rectangle.
"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """Initialization of Constructor.

        Args:
            width(int): Width of the rectangle.
            height(int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter to retrieve it"""

        return self.__width
    @width.setter
    def width(self, value):
        """ """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get the height"""

        return self.__height
    @height.setter
    def height(self, value):
        """Set the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """That returns the area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):

        """That returns the rectangula's perimeter"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ """

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for x in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"

            return rectangle_str.rstrip()

    def __repr__(self):
        """Return a string representation of the rectangle."""

        return f"Rectangle({self.__width}, {self.__height})"
