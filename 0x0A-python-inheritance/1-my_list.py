#!/usr/bin/python3

"""class MyList"""


class MyList(list):
    """a class MyList."""
    def print_sorted(self):
        """
        A function that prints the list,
        but sorted (ascending sort).
        """
        print(sorted(self))
