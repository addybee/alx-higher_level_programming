#!/usr/bin/python3
def best_score(a_dictionary):
    key = list(a_dictionary)[0]
    max = a_dictionary[key]
    for k, v in a_dictionary.items():
        if v > max:
            max = v
            key = k
    return key
