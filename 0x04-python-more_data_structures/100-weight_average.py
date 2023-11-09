#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return sum(k[0] * k[1] for x in my_list]) / sum([k[1] for k in my_list])
