#!/usr/bin/python3
""" Square Unitest """

import unittest
from models.square import Square


class TestMaxInt(unittest.TestCase):
    """ class test """

    def test_obj(self):
        """ obj test """
        obj1 = Square(1)
        self.assertEqual(obj1.id, 6)
        self.assertEqual(obj1.width, 1)
        self.assertEqual(obj1.height, 1)
        self.assertEqual(obj1.x, 0)
        self.assertEqual(obj1.y, 0)

        obj2 = Square(2, 1)
        self.assertEqual(obj2.id, 7)
        self.assertEqual(obj2.width, 2)
        self.assertEqual(obj2.height, 2)
        self.assertEqual(obj2.x, 1)
        self.assertEqual(obj2.y, 0)

        obj3 = Square(3, 4, 1)
        self.assertEqual(obj3.id, 8)
        self.assertEqual(obj3.width, 3)
        self.assertEqual(obj3.height, 3)
        self.assertEqual(obj3.x, 4)
        self.assertEqual(obj3.y, 1)

        obj4 = Square(4, 5, 6, 102)
        self.assertEqual(obj4.id, 102)
        self.assertEqual(obj4.width, 4)
        self.assertEqual(obj4.height, 4)
        self.assertEqual(obj4.x, 5)
        self.assertEqual(obj4.y, 6)
