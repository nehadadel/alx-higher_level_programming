#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        sub_matrix = map(lambda num : num ** 2, row)
        squared_matrix.append(list(sub_matrix))
    return squared_matrix
