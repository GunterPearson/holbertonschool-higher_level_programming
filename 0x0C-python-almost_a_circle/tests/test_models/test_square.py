#!/usr/bin/python3
""" Test for square.py
"""


import unittest
from models import base, rectangle, square


class TestSqureMethods(unittest.TestCase):
    """Square tests"""

    def test_inherits(self):
        """ verify square inherits rectangle """

        rect = rectangle.Rectangle(1, 1)
        sqre = square.Square(1)

        self.assertTrue(issubclass(type(sqre), type(rect)))

if __name__ == '__main__':
    unittest.main()
