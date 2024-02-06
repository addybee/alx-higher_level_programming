#!/usr/bin/python3
"""Describes the MyInt class"""


class MyInt(int):
    """ inherits from int"""

    def __init__(self, myint):
        """constructor for initialization"""
        self.myint = myint

    def __eq__(int1, int2):
        """defines inverted == operaror"""
        return int1.myint != int2

    def __ne__(int1, int2):
        """defines inverted != operaror"""
        return int1.myint == int2
