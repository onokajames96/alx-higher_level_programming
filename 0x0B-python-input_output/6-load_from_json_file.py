#!/usr/bin/python3
"""
Module: 6-load_from_json_file.
"""
import json


def load_from_json_file(filename):
    """
    Load JSON data from a file and return the corresponding object.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The Python object created from the JSON data.
    """
    with open(filename, 'r') as file:
        return json.load(file)
