#!/usr/bin/python3
"""define a class Square"""


class Square:
    """defines a square by by private instance"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size (no type/value verification)

        Args:
            size (int): the size of the square.
            position (tuple): coordinates
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve the size of the square"""
        return position

    @position.setter
    def position(self, value):
        """set the size of the square
        Args:
            value (tuple): coordinate
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        [print("") for idx in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for y in range(0, self.__size)]
            print("")

     def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
