#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print a list of integer in revese"""
    for k in reversed(my_list):
        print("{:d}".format(k))
