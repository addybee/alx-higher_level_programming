#!/usr/bin/python3
"""this module defines a  function that prints a square with the character #
"""


def print_square(size):
    """prints a square with the character #

    Args:
        size (int):  is the size length of the square
    Raise:
        TypeError: with the message "size must be an integer"
        ValueError: with the message size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print()
    else:
        for i in range(size):
            print("#" * size)
