#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        for j in i:
            new_matrix[i][j] = j * j
            return new_matrix
