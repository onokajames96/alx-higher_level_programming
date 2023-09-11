#!/usr/bin/python3

"""defines the function"""

def is_same_class(obj, a_class):
    """check if an object is exactly an instance of a specified class
    using the type(). function"""

    return type(obj) is a_class
