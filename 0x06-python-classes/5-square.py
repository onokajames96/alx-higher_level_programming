#!/usr/bin/python3
"""A class Square that defines a square.
"""
class Square:
    """Object Square. """
    def __init__(self, size=0):
        """Initialization.
        Args:
            size (int): The size of the  square.

        """
        self.__size = size

    @property
    def size(self):
        """Retrival.
        """

        return self.__size
    @size.setter
    def size(self, value):
        """sets it.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ that returns the current square area.
        """
        return self.__size * self.__size

     def my_print(self):



         if self.__size == 0:
             print("")
         else:
              for x in range(0, self.__size):
                  for y in range(0, self.__size):
                      print("#", end="")
                  print()
