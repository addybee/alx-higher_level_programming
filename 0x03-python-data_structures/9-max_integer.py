#!/usr/bin/python3
def max_integer(my_list=[]):
    if not list:
        return None
    maxi = 0
    for i in range(len(my_list)):
        if maxi < my_list[i]:
            maxi = my_list[i]
    return maxi
