#!/usr/bin/python3
""" Rectangle File """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ square initialization """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str print """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """ returns square size """
        return self.height
    
    @size.setter
    def size(self, size):
        self.height = size
        self.width = size
