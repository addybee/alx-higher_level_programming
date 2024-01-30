#!/usr/bin/python3
"""Module contain class LockedClass with no class or object attribute, that
    prevents the user from dynamically creating new instance attributes, except
    if the new instance attribute is called first_name.
"""


class LockedClass:
    """Class with locked down attributes. Can only add first_name"""

    def __setattr__(self, fname, value):
        if fname != "first_name":
            raise AttributeError("new instance attribute should be first_name")
        else:
            self.__dict__[fname] = value
