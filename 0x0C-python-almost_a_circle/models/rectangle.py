#!/usr/bin/python3
"""rectangle class defined"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): The width.
            height (int): The height.
            x (int): x-coordinate.
            y (int): y-coordinate.
            id (int, optional): ID.

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x-coordinate with validation."""
        if not isinstance(value, int):
            raise ValueError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y-coordinate with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns:
            int: The area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance to stdout."""
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle instance.

        Args:
            *args: Positional arguments (id, width, height, x, y).
            **kwargs: Keyword arguments (attribute=value pairs).
        """
        if args:
            attr = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], arg)
        elif kwargs:
            for key, v in kwargs.items():
                self.__setattr__(key, v)

    def to_dictionary(self):
        """
        That returns the dictionary representation of a Rectangle.
        """
        return {
                "id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y
                }

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        s = ("[Rectangle] ({}) {}/{} - {}/{}"
             .format(self.id, self.__x, self.__y, self.__width,
                     self.__height))
        return s
