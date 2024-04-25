#!/usr/bin/python3
"""  finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """finds a peak

    Args:
        list_of_integers (list): the provided list

    Returns:
        int: a peak in the list
    """
    sorted_list = sorted(list_of_integers)
    size = len(list_of_integers)
    if size == 0:
        return None
    return sorted_list[size - 1]
