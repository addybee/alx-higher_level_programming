#!/usr/bin/python3
"""define a class Square"""


class Square:
    """defines a square by by private instance"""
    def __init__(self, size=0):
        """Instantiation with size (no type/value verification)

        Args:
            size (int): the size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
