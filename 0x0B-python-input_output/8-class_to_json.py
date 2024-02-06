#!/usr/bin/python3
""" defines a function that  returns the dictionary description with simple
    data structure
"""


def class_to_json(obj):
    """ returns the dictionary description with simple data structure """

    result = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("__"):
            if isinstance(value, (list, dict, str, int, bool)):
                result[key] = value
    return result
