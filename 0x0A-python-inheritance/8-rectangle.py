#!/usr/bin/python3
"""
A class 'Rectangle' derived from 'BaseGeometry'.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class called Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
