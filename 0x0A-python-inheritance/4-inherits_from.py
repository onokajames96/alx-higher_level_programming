#!/usr/bin/python3
"""Sub class"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an
    inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to check if the object's class inherits from.

    Returns:
        True if the object is an instance of a class that
        inherited from the specified class; otherwise, False.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
