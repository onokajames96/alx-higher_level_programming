#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """defines a rectnangle.
    """
    def __init__(self, width=0, height=0):
        """Initialization.

        Args:
            width (int): the rectangle's width.
            height (int): the rectangle's height.
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width."""

        return self.__width

    @width.setter
    def width(self, value):

        """Set the width."""

        if type(value) is not int:

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Gets the height."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets it."""

        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """the rectangle area."""

        return self.__width * self.__height

    def perimeter(self):
        """The rectangle perimeter.
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        representation of the rectangle.
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""

        for _ in range(self.__height):
            rectangle_str += "{}".format("#" * self.__width)
            if _ < self.__height - 1:
                rectangle_str += "\n"

            return rectangle_str

    def __repr__(self):
        """__repr__
        Returns:
        string representation of rectangle.
        """
        return super().__repr__()
