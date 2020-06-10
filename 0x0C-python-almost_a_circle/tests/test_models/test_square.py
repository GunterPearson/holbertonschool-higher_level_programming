#!/usr/bin/python3
"""Module to test square
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """ test for square __init__"""

    def test_base(self):
        """ test for square __init__"""
        self.assertIsInstance(Square(10), Base)

    def test_rectangle(self):
        """ test for square __init__"""
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        """ test for square __init__"""
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """ test for square __init__"""
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        """ test for square __init__"""
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        """ test for square __init__"""
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        """ test for square __init__"""
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_more_than_four_args(self):
        """ test for square __init__"""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_private(self):
        """ test for square __init__"""
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        """ test for square __init__"""
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_height_getter(self):
        """ test for square __init__"""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.height)

    def test_x_getter(self):
        """ test for square __init__"""
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        """ test for square __init__"""
        self.assertEqual(0, Square(10).y)

    def test_size_setter(self):
        """ test for square __init__"""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_width_getter(self):
        """ test for square __init__"""
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.width)
