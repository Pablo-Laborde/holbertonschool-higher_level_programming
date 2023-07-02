#!/usr/bin/python3
""" Rectangle Unitest """

import unittest
from models.base import Base


class TestMaxInt(unittest.TestCase):
    """ class test """

    def test_obj(self):
        """ obj test """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

        obj3 = Base(100)
        self.assertEqual(obj3.id, 100)
