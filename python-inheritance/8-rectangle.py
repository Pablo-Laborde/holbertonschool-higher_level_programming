#!/usr/bin/python3
""" Ex 8 """


class BaseGeometry():
    """ Basegeometry class """
    def area(self):
        """ area function """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ int val function """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """ Rectangle class """

    """ variables """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """ init """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        __width = width
        __height = height
