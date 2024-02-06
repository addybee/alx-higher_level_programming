#!/usr/bin/python3
""" defines a function that returns True if the object is an instance of, or
    if the object is an instance of a class that inherited from, the specified
    class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """check if  Same class or inherit from

    Args:
        obj (object): object
        a_class (class): class

    Returns: true or false
    """
    return type(obj) == a_class or issubclass(obj, a_class)
