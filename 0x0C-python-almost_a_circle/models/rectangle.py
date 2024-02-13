#!/usr/bin/python3
""" defines a rectangle """


from models.base import Base


class Rectangle(Base):
    """ defines rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        Rectangle.validate("width", width)
        Rectangle.validate("height", height)
        Rectangle.validate("x", x)
        Rectangle.validate("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @staticmethod
    def validate(name, value):
        """this function is for validating the setters"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ retrieve width """
        return self.__width

    @property
    def height(self):
        """ retrieve height """
        return self.__height

    @width.setter
    def width(self, value):
        """ sets the width """
        Rectangle.validate("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the height """
        Rectangle.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """ retrieve x """
        return self.__x

    @property
    def y(self):
        """ retrieve width """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y """
        Rectangle.validate("y", value)
        self.__y = value

    @x.setter
    def x(self, value):
        """ sets the x """
        Rectangle.validate("x", value)
        self.__x = value

    def area(self):
        """calculate area of a rectangle

        Returns:
            int: the area
        """
        return self.__height * self.__width

    def display(self):
        """prints in stdout the rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        for i in range(self.height):
            print(" " * self.__x + "#" * self.width)

    def __str__(self):
        """ return the following rectangle description: [Rectangle]
            (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """ Update the class Rectangle """
        if args is not None:
            names = ["id", "width", "height", "x", "y"]
            for name, val in zip(names, args):
                Rectangle.validate(name, val)
                setattr(self, name, val)

        if kwargs is not None:
            for key, value in kwargs.items():
                if key in kwargs:
                    Rectangle.validate(key, value)
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary description rectangle """

        result = {"id": self.id, "width": self.width, "height": self.height,
                  "x": self.x, "y": self.y}
        return result
