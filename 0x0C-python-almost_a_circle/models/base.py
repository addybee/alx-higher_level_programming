#!/usr/bin/python3
""" defines a class Base that will be the “base” of all other classes in this
    project
"""


import json


class Base:
    """ manage attribute in all future classes and avoid code duplication """

    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON representation of a list of dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        try:
            return json.dumps(list_dictionaries)
        except Exception:
            return "[]"

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        new_obj = None

        if dictionary is None:
            return None
        if cls.__name__ == "Rectangle":
            new_obj = Rectangle(1, 1, 0, 0, 0)
            new_obj.update(**dictionary)
            return new_obj
        elif cls__name__ == "Square":
            new_obj = Square(1, 0, 0, 0)
            new_obj.update(**dictionary)
            return new_obj

    @classmethod
    def save_to_file(cls, list_objs):
        file_n = "{}.json".format(cls.__name__)
        if list_objs is None:
            with open(file_n, "w", encoding="utf-8") as f:
                json.dump([], f)
                return

        objs_str = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs],
        )
        with open(file_n, "w", encoding="utf-8") as f:
            f.write(objs_str)

    @classmethod
    def load_from_file(cls):
        """  returns a list of instances: """
        obj_list = []
        file_n = "{}.json".format(cls.__name__)
        try:
            with open(file_n, "r", encoding="utf-8") as myFile:
                json_string = cls.from_json_string(myFile.read())
                for o in json_string:
                    obj_list.append(cls.create(**o))
        except FileNotFoundError:
            pass
        return obj_list
