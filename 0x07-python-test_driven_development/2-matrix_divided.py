#!/usr/bin/python3
"""
Module 2-matrix_divided
funnction:
matrix_divided
"""


def matrix_divided(matrix, div):
    """
    matrix division
    """
    s = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(s)
    result = all(type(y) in [int, float] for row in matrix for y in row)
    if not result:
        raise TypeError(s)
    r = all(len(row) == len(matrix[0]) for row in matrix)
    if not r:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = [[round((x / div), 2) for x in row] for row in matrix]
    return new
