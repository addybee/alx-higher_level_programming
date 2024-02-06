#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """check if obj is the same type as a_class"""
    return type(obj) == a_class
