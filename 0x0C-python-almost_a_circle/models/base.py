#!/usr/bin/python3
""" defines a class Base that will be the “base” of all other classes in this
    project
"""


class Base:
    """ manage attribute in all future classes and avoid code duplication """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
