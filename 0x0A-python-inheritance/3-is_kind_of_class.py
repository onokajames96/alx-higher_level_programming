#!/usr/bin/python3
#Onoka James
"""Checks if its an object or a_class """

def is_kind_of_class(obj, a_class):
    """
    Determine if an object is an instance of, or inherits from, a specific class.

    Args:
        obj: The object to examine.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of or inherits from the specified class; otherwise, False.
    """
    if isinstance(obj, a_class):
        return True
    return False


