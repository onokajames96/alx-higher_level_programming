#!/usr/bin/python3
# Write a class Rectangle that inherits from BaseGeometry.

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiates a new Rectangle"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns:
            the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns:
            A string representation of the Rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
