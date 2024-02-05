#!/usr/bin/python3
"""class MyList that inherits from list:
"""


class MyList(list):
    """class MyList that inherits from list

    Args:
        list (parent): parent or super class
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
