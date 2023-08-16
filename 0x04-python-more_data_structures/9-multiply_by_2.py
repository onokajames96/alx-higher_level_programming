#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, result in a_dictionary.items():
        new[key] = result * 2
    return new
