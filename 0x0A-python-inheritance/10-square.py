#!/usr/bin/python3
"""Defination of a  Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square representation."""
    def __init__(self, size):
        """Initializes a new square.
        Args:
            size (int): The new square's size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
