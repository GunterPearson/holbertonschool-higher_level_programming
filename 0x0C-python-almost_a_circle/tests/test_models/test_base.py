#!/usr/bin/python3
"""Test for _blank_
"""


import unittest
from models import base
import pep8
import json


class TestBaseMethods(unittest.TestCase):
    """Testing Base class"""

    def test_instance_counter(self):
        """should keep track of number of instances as id
        """

        b1 = base.Base()
        start = b1.id
        b2 = base.Base()
        b3 = base.Base()
        b4 = base.Base()
        b5 = base.Base()
        self.assertEqual(b2.id, start + 1)
        self.assertEqual(b3.id, start + 2)
        self.assertEqual(b5.id, start + 4)

    def test_id_set(self):
        """ id can be set on instantiation
        """

        b1 = base.Base()
        b2 = base.Base(5)
        b3 = base.Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """ test list_dictionary conversion to json string """

        pass

    def test_from_json_string(self):
        """ test json string conversion to list_dictionary """

        pass

    def test_create(self):
        """ test creation of object from dict """

        pass

    def test_load_from_file(self):
        """ test loading an object from a file """

        pass

    def test_save_to_file(self):
        """ test saving to json file """

        pass

    def test_pep8_conformance(self):
        """load_from_file Docstring Test"""
        print("test_test_pep8_conformance")
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
