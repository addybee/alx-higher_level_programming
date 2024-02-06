#!/usr/bin/python3
"""define a function that returns an object (Python) from JSON string"""
from json import loads


def from_json_string(my_str):
    """ returns an object (Python data structure) """
    return loads(my_str)
