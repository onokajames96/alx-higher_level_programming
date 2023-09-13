#!/usr/bin/python3
"""
Creates a function that defines pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle.
    """

    for x in range(n):
        print(' '*(n-x), end='')
        print(' '.join(str(11**x)))
