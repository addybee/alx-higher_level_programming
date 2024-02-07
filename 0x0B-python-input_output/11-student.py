#!/usr/bin/python3
"""defines a student class"""


class Student:
    """ defines a student"""

    def __init__(self, first_name, last_name, age):
        """constructor for instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns the dictionary description with simple data structure """

        result = {}
        flag = 0

        if type(attrs) == list:
            flag = 1
            for key in attrs:
                if type(key) is not str:
                    flag = 0
                    break

        if flag == 0:
            result = {key: value for key, value in self.__dict__.items()
                      if not key.startswith("__") and
                      isinstance(value, (list, dict, str, int, bool))}
            return result

        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for item in json:
            self.__dict__[item] = json[item]
