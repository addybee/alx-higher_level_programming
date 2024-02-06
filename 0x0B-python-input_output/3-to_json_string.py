#!/usr/bin/python3
"""define a function that returns the JSON representation of an object"""
from json import dumps


def to_json_string(my_obj):
    """ returns the JSON representation of an object """
    return dumps(my_obj)
