#!/usr/bin/python3
""" Rectangle File """

Base = __import__('base').Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, width):
        """ sets width """
        self.__width = width

    @property
    def height(self):
        """ return height """
        return self.__height

    @height.setter
    def height(self, height):
        """ sets height """
        self.__height = height

    @property
    def x(self):
        """ return x """
        return self.__x

    @x.setter
    def x(self, x):
        """ sets x """
        self.__x = x

    @property
    def y(self):
        """ return y """
        return self.__y

    @y.setter
    def y(self, y):
        """ sets y """
        self.__y = y
