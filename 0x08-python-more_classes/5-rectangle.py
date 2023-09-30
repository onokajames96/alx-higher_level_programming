#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by:"""


class Rectangle:
    """class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization.

        Args:
            width(int): Rectangles width.
            height(int): Height of the rectangle.

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""

        if type(value) is not int:
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
        """Sets the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and returns the area"""

        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle's perimetre"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """string representation of the rectangle defined"""

        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self._height):
            rectangle_str += "#" * self._width
            if x < self._height - 1:
                rectangle_str += "\n"

        return rectangle_str

    def __repr__(self):
        """Returns string representation of the rectangle"""

        return f"Rectangle({self._width}, {self._height})"

    def __del__(self):
        """print message when deleted"""

        print("Bye rectangle...")
