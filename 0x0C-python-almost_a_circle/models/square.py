#!/usr/bin/python3
""" defines a Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return the following square description: [Square]
            (<id>) <x>/<y> - <size>
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    @property
    def size(self):
        """retrieve size"""
        return self.width

    @size.setter
    def size(self, size):
        """ sets the size """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update the class Square """
        if args is not None and len(args) > 0:
            names = ["id", "size", "x", "y"]
            for name, val in zip(names, args):
                Rectangle.validate(name, val)
                setattr(self, name, val)
        elif kwargs is not None:
            for key, value in kwargs.items():
                if key in kwargs:
                    Square.validate(key, value)
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary description Square """
        result = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return result
