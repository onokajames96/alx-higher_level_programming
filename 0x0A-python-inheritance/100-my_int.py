#!/usr/bin/python3
"""Write a class MyInt that inherits from int."""


class MyInt(int):
    """ A custom integer class that inherits from int."""

    def __eq__(self, other):
        """Overrides the equality operator (==)."""

        return False

    def __ne__(self, other):
        """Overrides the inequality operator (!=)."""

        return True
