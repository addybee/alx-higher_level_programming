#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''
    square_matrix_simple - computes the square value of all integers of a
    matrix.
    @matrix: is a 2 dimensional array
    '''
    return [[y ** 2 for y in x] for x in matrix]
