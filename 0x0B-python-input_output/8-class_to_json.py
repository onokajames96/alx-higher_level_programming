#!/usr/bin/python3
"""
Module: 8-class_to_json.py

This module contains a function that Convert an object to a dictionary
"""


def class_to_json(obj):
    """
    Args:
        obj: An instance of a class with serializable attributes.
    Returns:
        the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object:
    """
    return obj.__dict__
