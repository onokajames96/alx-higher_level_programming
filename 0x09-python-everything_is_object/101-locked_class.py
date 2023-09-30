#!/usr/bin/python3
"""A class LockedClass."""


class LockedClass:
    """
    A class that prevents the user from dynamically
    creating new instance attributes except 'first_name'.
    """
    __slots__ = ["first_name"]
