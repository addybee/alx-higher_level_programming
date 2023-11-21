#!/usr/bin/python3
"""define a class Square"""


class Square:
    """defines a square by by private instance"""
    def __init__(self, size=0):
        """Instantiation with size (no type/value verification)

        Args:
            size (int): the size of the square.
        """

        try:
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
