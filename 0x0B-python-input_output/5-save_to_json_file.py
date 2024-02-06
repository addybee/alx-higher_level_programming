#!/usr/bin/python3
"""define a function that writes an Object to a text file, using a JSON rep"""
from json import dump


def to_json_string(my_obj, filename):
    """ this function writes an object to file """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        dump(my_obj, myFile)
