#!/usr/bin/python3
""" defines a function that inserts a line of text to a file, after each line
    containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    with open(filename, "r+") as myFile:
        text = ""
        for line in myFile:
            if search_string in line:
                line += new_string
            text += line
        myFile.seek(0)
        myFile.write(text)
