#!/usr/bin/python3
""" unitest file """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """ class """
    def test_max_int(self):
        """ test fucntion """
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-2, -3, -4, -8]), -2)

    def test_val(self):
        """ test fucntion """
        self.assertRaises(TypeError, max_integer("hola"), 2)
