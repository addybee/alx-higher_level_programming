#!/usr/bin/python3
"""define a function that  creates an Object from a “JSON file”"""
from json import load


def load_from_json_file(filename):
    """  creates an Object from a “JSON file” """

    with open(filename, mode="r", encoding="utf-8") as myFile:
        return load(myFile)
