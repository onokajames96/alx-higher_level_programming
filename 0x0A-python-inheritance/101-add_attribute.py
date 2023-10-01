#!/usr/bin/python3
"""
Defination of a function tha add new atrribute to an object.
"""


def add_attribute(obj, attr, value):
    """
    A function that adds a new attribute to an object if it’s possible.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
