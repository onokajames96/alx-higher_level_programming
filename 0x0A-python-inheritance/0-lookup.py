#!/usr/bin/python3
# James Onoka

"""Create lookup function"""

def lookup(obj):
    """That returns the list containing strings representing
    the attributes and methods of the object."""

    return dir(obj)
