#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
        return []
    new_matrix = [[y ** 2 for y in matrix[x]] for x in range(len(matrix))]
    return new_matrix
