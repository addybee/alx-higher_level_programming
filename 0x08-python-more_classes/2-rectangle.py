#!/usr/bin/python3
"""defines a Rectangle class
"""


class Rectangle:
    """class that define rectangle
    """
    def __init__(self, width=0, height=0):
        """initializes the instance attribute

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve Private instance attribute (width)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """changes the width instance attribute

        Args:
            value (int): the width to be set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieve Private instance attribute: height
        """
        return self.__height

    @height.setter
    def height(self, value):

        """set the new height of the rectaangle

        Args:
            value (int): new height of rectangle

        Raises:
            TypeError: if not an integer
            ValueError: if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """calculate area of a rectangle

        Returns:
            int: the area
        """
        return self.__height * self.__width

    def perimeter(self):
        """perimeter of rectangle

        Returns:
            int: perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__width + self.__height))
