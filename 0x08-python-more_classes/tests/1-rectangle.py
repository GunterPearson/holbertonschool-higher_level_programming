#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
Rectangle = __import__('1-rectangle').Rectangle


class TestRectangle(unittest.TestCase):

    def setUp():
        rect = Rectangle(2, 4)

    def test_doct(self):
        self.assertAlmostEqual(rectangle.__dict__, {'_Rectangle__height': 4, '_Rectangle__width': 2})