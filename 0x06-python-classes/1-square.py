#!/usr/bin/python3
"""define a class Square"""
class Square:
    """defines a square by by private instance"""

    def __init__(self, size):
        """Instantiation with size (no type/value verification)

        args:
            size (int): the size of the square.
        """

        self.__size = size
