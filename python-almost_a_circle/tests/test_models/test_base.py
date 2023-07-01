#!/usr/bin/python3
""" Rectangle Unitest """

import unittest
from models.base import Base


class TestMaxInt(unittest.TestCase):
    """ class test """

    def test_obj(self):
        """ obj test """
        obj1 = Base()
        self.assertEqual(self.id, 1)

        obj2 = Base()
        self.assertEqual(self.id, 2)

        obj3 = Base(10)
        self.assertEqual(self.id, 10)
