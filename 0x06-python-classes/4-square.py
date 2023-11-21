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
        """retrieve the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square
        Args:
            value (int): new size to be set
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
