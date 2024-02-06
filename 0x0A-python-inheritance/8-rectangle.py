#!/usr/bin/python3
"""define an empty class BaseGeometry"""


class BaseGeometry:
    """ empty class BaseGeometry"""

    def area(self):
        """raises an Exception with the message area() is not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """this class inherit from BaseGeometry"""

    def __init__(self, width, height):
        """constructor for Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
