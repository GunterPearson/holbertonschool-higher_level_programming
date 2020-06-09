#!/usr/bin/python3
"""Module to test base.Base
"""
import unittest
from models import base


class Testbase_Methods(unittest.TestCase):
    """Testing base.Base class"""

    def test_id(self):
        """ test different id """

        b1 = base.Base()
        start = b1.id
        b2 = base.Base()
        b3 = base.Base()
        self.assertEqual(b2.id, start + 1)
        self.assertEqual(b3.id, start + 2)

    def test_id(self):
        """ test id with id set """
        b1 = base.Base()
        b2 = base.Base(5)
        b3 = base.Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 5)
        self.assertEqual(b3.id, 2)

    def test_unique_id(self):
        """ test uniq """
        b1 = base.Base()
        b2 = base.Base(12)
        b3 = base.Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_to_json(self):
        """ test to json string """
        pass

    def test_from_json_string(self):
        """ test from json string """
        pass

    def test_dict(self):
        """ test creating dict"""
        pass

    def test_json_to_file(self):
        """ test save to file """
        pass

    def test_from_file(self):
        """ test from file """
        pass

if __name__ == '__main__':
    unittest.main()
