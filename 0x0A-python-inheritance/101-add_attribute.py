#!/usr/bin/python3
"""Describs a function that safely adds attributes to an object"""


def add_attribute(obj, name, value):
    """define the fuction add attributes"""

    if hasattr(obj, '__dict__') or hasattr(type(obj), '__slots__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
