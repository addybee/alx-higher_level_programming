#!/usr/bin/python3
# return c if a is less than b or a+b if c is greater than b else a*b-c
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
