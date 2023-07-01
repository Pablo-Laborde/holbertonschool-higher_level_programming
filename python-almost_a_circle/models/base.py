#!/usr/bin/python3
""" Base File """

import json


class Base():
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json string """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """ to json file """
        filename = f"{cls.__class__.__name__}.json"
        with open(filename, "w") as o_file:
            o_file.write(cls.to_json_string(list_objs))
