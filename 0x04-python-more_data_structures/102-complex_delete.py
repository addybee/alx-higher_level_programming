#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    for item in a_dictionary.copy():
        if a_dictionary[item] == value:
            del a_dictionary[item]
    return a_dictionary
