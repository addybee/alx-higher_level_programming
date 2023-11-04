#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lst_a = list(tuple_a)
    lst_b = list(tuple_b)
    while len(lst_a) < 2:
        lst_a.append(0)
    while len(lst_b) < 2:
        lst_b.append(0)
    return tuple(i + j for i, j in zip(lst_a[:2], lst_b[:2]))
