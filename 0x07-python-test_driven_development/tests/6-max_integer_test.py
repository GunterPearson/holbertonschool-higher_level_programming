#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -40, -2, -8]), -1)

    def test_type(self):
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, [1, "hello", 3])

    def test_value(self):
        self.assertEqual(max_integer([2.83, 2.22, 2.01]), 2.83)
