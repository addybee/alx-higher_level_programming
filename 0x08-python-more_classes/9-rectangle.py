#!/usr/bin/python3
"""defines a Rectangle class
"""


class Rectangle:
    """class that define rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
        self.__width = value

    @property
    def height(self):
        """retrieve Private instance attribute: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the new height

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
        self.__height = value

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
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character # when str() and print() use
        it as argument

        Returns:
            str: rectangle with the character #
        """
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        for row in range(self.__height):
            result += (str(self.print_symbol) * self.__width)
            if row != (self.__height - 1):
                result += "\n"
        return result

    def __repr__(self):
        """string representation

        Returns:
            str: string representation of the rectangle to be able to recreate
            a new instance by using eval()
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print the message Bye rectangle... (... being 3 dots not ellipsis)
            when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area >= rect_2.area else rect_2)

    @classmethod
    def square(cls, size=0):
        """ createa new Rectangle instance with width == height == size

        Args:
            size (int, optional): size of the square. Defaults to 0.

        Returns:
            Rectangle:  new Rectangle instance with width == height == size
        """
        return cls(size, size)
