#!/usr/bin/python3
"""Module to test base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """ First base tests """

    def test_no_arg(self):
        """ test no arguments """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """ test id value """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """ test id if none is passed """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_un_id(self):
        """ test uniq id """
        self.assertEqual(12, Base(12).id)

    def test_after_unique_id(self):
        """ test after uniq """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """ test public id """
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """ test private """
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        """ test str """
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        """ test float """
        self.assertEqual(5.5, Base(5.5).id)

    def test_dict_id(self):
        """ test dict """
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        """ test bool """
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        """ test list """
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_two_args(self):
        """ test two """
        with self.assertRaises(TypeError):
            Base(1, 2)

if __name__ == "__main__":
    unittest.main()
