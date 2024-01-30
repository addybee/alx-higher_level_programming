#!/usr/bin/python3
"""this module contains a function that divides all elements of a matrix
    matrix must be a list of lists of integers or floats and Each row of
    the matrix must be of the same size, otherwise raise a TypeError.
    div must be a number (integer or float), otherwise raise a TypeError
    exception with the message div must be a number div can’t be equal to 0
    .otherwise raise a ZeroDivisionError exception with the message
    division by zero. All elements of the matrix should be divided by div,
    rounded to 2 decimal places, Returns a new matrix.
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (list):  list of lists of integers or floats
        div (int, float): a number (integer or float) that divides
    Return:
        a new matrix
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    for inner_list in matrix:
        if not isinstance(inner_list, list):
            raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats")
        for element in inner_list:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
    if (not all(len(inner_arr) == len(matrix[0]) for inner_arr in matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = list(map(lambda x: list(map(lambda z: round(z / div, 2), x)),
                      matrix))
    return result
