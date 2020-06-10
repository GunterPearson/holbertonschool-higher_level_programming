#!/usr/bin/python3
""" Test for square.py
"""


import unittest
from models import base, rectangle, square
import pep8
import json


class TestSqureMethods(unittest.TestCase):
    """Square tests"""

    def test_inherits(self):
        """ verify square inherits rectangle """

        rect = rectangle.Rectangle(1, 1)
        sqre = square.Square(1)

        self.assertTrue(issubclass(type(sqre), type(rect)))

    def test_pep8_conformance(self):
        """load_from_file Docstring Test"""
        print("test_test_pep8_conformance")
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
