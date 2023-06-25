#!/usr/bin/python3
""" Ex 8 """

BG = __import__('7-base_geometry').BaseGeometry


class Rectangle(BG):
    """ Rectangle class """

    """ variables """
    __width = int
    __height = int

    def __init__(self, width, height):
        """ init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        __width = width
        __height = height
