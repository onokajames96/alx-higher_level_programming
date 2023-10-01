#!/usr/bin/python3
"""
Creates a function that defines pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to 'n' rows.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        rows = triangle[-1]
        temp = [1]

        for num in range(len(rows) - 1):
            temp.append(rows[num] + rows[num + 1])
        temp.append(1)
        triangle.append(temp)

    return triangle
