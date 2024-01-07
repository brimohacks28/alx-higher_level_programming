#!/usr/bin/python3
# 6-print_matrix_integer.py
# Brian Maema codes


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for a in range(len(matrix)):
        for j in range(len(matrix[a])):
                print("{:d}".format(matrix[a][j]), end="")
                if j != (len(matrix[a]) - 1):
                    print(" ", end="")

        print("")
