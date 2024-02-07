#!/usr/bin/python3
""" defines a function thatthat returns a list of lists of integers
    representing the Pascal’s triangle of n"""


def comb(n, r):
    """returns n combination r"""
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        return n * factorial(n-1)

    return round(factorial(n) / (factorial(n - r) * factorial(r)))


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s triangle
    of n"""

    return [[comb(m, r) for r in range(m + 1)] for m in range(n)]
