#!/usr/bin/python3
"""Defination of class Rectangle."""


class Rectangle:
    """Class representing rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization."""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """Gets the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets/retrieves the height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Gets the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Rectangles area returned."""
        return self.width * self.height

    def perimeter(self):
        """Rectangles perimeter returned."""
        if self.width == 0 or self.height == 0:
            return 0

        else:
            return 2 * (self.width + self.height)

    def __repr__(self):
        """
        A string representation of
        the rectangle using print_symbol returned.
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __str__(self):
        """Rectangles string representation returned."""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""

        for num in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + "\n"

        return rectangle_str[:-1]

    def __del__(self):
        """Destructor called when the instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """A function that returns the biggest rectangle based on the area."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size."""
        return cls(size, size)
