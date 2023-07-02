#!/usr/bin/python3
""" Rectangle Unitest """

import unittest
from models.rectangle import Rectangle


class TestMaxInt(unittest.TestCase):
    """ class test """

    def test_obj(self):
        """ obj test """
        obj1 = Rectangle(1, 1)
        self.assertEqual(obj1.id, 3)
        self.assertEqual(obj1.width, 1)
        self.assertEqual(obj1.height, 1)
        self.assertEqual(obj1.x, 0)
        self.assertEqual(obj1.y, 0)

        obj2 = Rectangle(2, 3, 1)
        self.assertEqual(obj2.id, 4)
        self.assertEqual(obj2.width, 2)
        self.assertEqual(obj2.height, 3)
        self.assertEqual(obj2.x, 1)
        self.assertEqual(obj2.y, 0)

        obj3 = Rectangle(3, 4, 1, 1)
        self.assertEqual(obj3.id, 5)
        self.assertEqual(obj3.width, 3)
        self.assertEqual(obj3.height, 4)
        self.assertEqual(obj3.x, 1)
        self.assertEqual(obj3.y, 1)

        obj4 = Rectangle(4, 5, 6, 7, 101)
        self.assertEqual(obj4.id, 101)
        self.assertEqual(obj4.width, 4)
        self.assertEqual(obj4.height, 5)
        self.assertEqual(obj4.x, 6)
        self.assertEqual(obj4.y, 7)
