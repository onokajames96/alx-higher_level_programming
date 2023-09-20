#!/usr/bin/python3
"""Module for the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square class.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): The identifier of the square.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square."""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the square's attributes"""
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
            else:
                for key, v in kwargs.items():
                    self.__setattr__(key, v)

    def to_dictionary(self):
        """Returns the dictionary represantation of the class square."""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
