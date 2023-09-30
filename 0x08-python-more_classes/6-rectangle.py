#!/usr/bin/python3
"""
A class rectangle defined.
"""


class Rectangle:
    """
    A class representing a rectangle.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialization of the rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Get/retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Area of the rectangle returned."""
        return self.width * self.height

    def perimeter(self):
        """A function that returns the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """ Retuns string/print the rectangle with the character #."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""

        for i in range(self.height):
            rectangle_str += "{}".format("#" * self.__width)
            if i < self.__height - 1:
                rectangle_str += "\n"

        return rectangle_str

    def __repr__(self):
        """
        return a string representation of the rectangle
        to be able to recreate a new instance by using eval().
        """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor called when instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
