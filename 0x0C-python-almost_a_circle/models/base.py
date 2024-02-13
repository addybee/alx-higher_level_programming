#!/usr/bin/python3
""" defines a class Base that will be the “base” of all other classes in this
    project
"""


from json import loads


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
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return loads(json_string)

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
