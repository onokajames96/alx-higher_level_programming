#!/usr/bin/python3

"""Division of matrix."""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list[list]): The matrix to be divided.
        div (int or float): The divisor.

    Returns:
        list[list]: A new matrix with the elements divided by the divisor.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")


    if div == 0:
        raise ZeroDivisionError("division by zero")


    if not all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    """Check if all rows have the same length.
    """
    if len(set(len(row) for row in matrix)) > 1:

        raise ValueError("Each row of the matrix must have the same size")

    result_matrix = [[round(val / div, 2) for val in row] for row in matrix]

    return result_matrix
