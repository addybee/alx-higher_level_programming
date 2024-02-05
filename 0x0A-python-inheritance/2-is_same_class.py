#!/usr/bin/python3
"""function that returns True if the object is exactly an instance
of the specified class
"""


def is_same_class(obj, a_class):
    """_summary_

    Args:
        obj (object): object to be check
        a_class (class): the class

    Returns:
        bool: True if instance else False
    """
    if isinstance(obj, a_class):
        return True
    return False
