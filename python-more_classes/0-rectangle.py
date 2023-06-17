#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ class def """
    __length = 0
    __width = 0

    def __init__(self, length=0, width=0):
        """ init """
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length):
        if type(length) != int:
            raise TypeError("length must be an integer")
        if length < 0:
            raise ValueError("length must be >= 0")
        self.__length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
