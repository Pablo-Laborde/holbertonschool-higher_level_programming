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
