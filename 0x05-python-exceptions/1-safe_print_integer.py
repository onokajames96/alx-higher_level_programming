#!/usr/bin/python3
def safe_print_integer(value):
    """ printing an integer"""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
