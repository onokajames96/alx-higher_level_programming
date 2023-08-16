#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square =[]
    for y in matrix:
        square.append(list(map(lambda x: x * x,  y)))
    return square
