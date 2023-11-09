#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = list(a_dictionary)[0]
    max = a_dictionary[key]
    for k, v in a_dictionary.items():
        if max < v:
            max = v
            key = k
    return key
