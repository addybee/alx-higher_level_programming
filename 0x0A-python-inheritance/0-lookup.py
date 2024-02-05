#!/usr/bin/python3
"""contain function that returns the list of available attributes and
    methods of an object:
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object:

    Args:
        obj (_type_): object whose attribute and method are to be returned

    Returns:
        list: returns the list of available attributes and methods of an object
    """
    return dir(obj)
