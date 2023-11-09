#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    nth = 0
    total = 0
    for y, z in my_list:
        nth += z
        total += (y * z)
    return total / nth
