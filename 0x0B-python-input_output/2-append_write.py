#!/usr/bin/python3
"""defines a function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """this function returns the number of characters added to a file"""

    if type(filename) is not str or type(text) is not str:
        raise TypeError("filename and text must be string")
    with open(filename, mode="a", encoding="utf-8") as myFile:
        result = myFile.write(text)
        return result
