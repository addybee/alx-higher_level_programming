#!/usr/bin/python3
"""  finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """finds a peak

    Args:
        list_of_integers (list): the provided list

    Returns:
        int: a peak in the list
    """
    size = len(list_of_integers)
    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    n = (size + 1) // 2
    left = find_peak(list_of_integers[0:n])
    right = find_peak(list_of_integers[n:size])
    if left > right:
        return left
    return right
