#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    for k, v in a_dictionary.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
