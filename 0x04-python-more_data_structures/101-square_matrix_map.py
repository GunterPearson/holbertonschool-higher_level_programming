#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix == [] or matrix is None:
        return []
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
