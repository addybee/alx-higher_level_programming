#!/usr/bin/env python3
def no_c(my_string):
    newString = ""
    for character in my_string:
        if character != "c" and character != "C":
            newString += character
    return newString
