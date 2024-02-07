#!/usr/bin/python3
"""defines a student class"""


class Student:
    """ defines a student"""

    def __init__(self, first_name, last_name, age):
        """constructor for instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns the dictionary description with simple data structure """

        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith("__"):
                if isinstance(value, (list, dict, str, int, bool)):
                    result[key] = value
        return result
