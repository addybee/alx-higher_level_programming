#!/usr/bin/python3
"""define an class Square that inherits from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this class inherit from Retangle"""

    def __init__(self, size):
        """constructor for Square class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
