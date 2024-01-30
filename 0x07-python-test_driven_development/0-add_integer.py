#!/usr/bin/python3
"""this module is for a function which adds two integer add_integer(a, b=98)
    a and b must be integers or floats, otherwise raise a TypeError exception
    with the message a must be an integer. b has default value of 98
"""


def add_integer(a, b=98):
    """this function adds two integers and return the result
        Args:
            a (int, float): first integer
            b (int, float, optional): second integer. Defaults to 98.
    """
    if (not isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    if (isinstance(a, float)):
        a = int(a)
    if (isinstance(b, float)):
        b = int(b)
    return a + b
