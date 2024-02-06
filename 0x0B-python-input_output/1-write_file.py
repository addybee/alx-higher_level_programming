#!/usr/bin/python3
"""defines a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of
        characters written
    """

    if type(filename) is not str or type(text) is not str:
        raise TypeError("filename and text must be string")
    with open(filename, mode="w", encoding="utf-8") as myFile:
        result = myFile.write(text)
        return result
