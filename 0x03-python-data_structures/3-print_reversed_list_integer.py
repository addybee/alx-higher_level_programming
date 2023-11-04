#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    nl = len(my_list)
    for idx in range(nl):
        print("{:d}".format(my_list[nl - 1 - idx]))
