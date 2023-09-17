#!/usr/bin/python3


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
         if not isinstance(value, int) or value <= 0:
             raise ValueError("Width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
         """Set height with validation."""
         if not isinstance(value, int):
             raise ValueError("Height must be a positive integer")
         self.__height = value
