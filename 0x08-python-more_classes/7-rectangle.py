#!/usr/bin/python3
"""Class rectangle defined."""


class Rectangle:
    """Class representing a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization.

        Args:
            width (int, optional): The rectangles width.
            height (int, optional): The rectangles height.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets/retrieves with attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width atrribute."""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/retrives the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns rectangles perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representing
        the rectangle with a specified symbol.
        """

        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""

        for num in range(self.height):
            rectangle_str = str(self.print_symbol) * self.width
            if num < self.__height - 1:
                rectangle_str += "\n"
            return rectangle_str

    def __repr__(self):
        """
        Return a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor called when isntance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
