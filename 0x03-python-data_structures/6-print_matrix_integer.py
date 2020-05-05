#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y < 2:
                print("{:d}".format(matrix[x][y]), end=" ")
            if y >= 2:
                print("{:d}".format(matrix[x][y]))
