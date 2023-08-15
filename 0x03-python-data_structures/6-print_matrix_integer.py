#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in range(len(row)):

            if num == len(row) - 1:
                print("{}".format(row[num]))
            else:
                print("{:d}".format(row[num]), end=" ")
