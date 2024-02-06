#!/usr/bin/python3
"""define an empty class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """this class inherit from BaseGeometry"""

    def __init__(self, width, height):
        """constructor for Rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ return the following rectangle description: [Rectangle]
            <width>/<height>
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
