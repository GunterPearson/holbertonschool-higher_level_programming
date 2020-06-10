#!/usr/bin/python3
""" Test for rectangle.py
"""


import unittest
from models import base, rectangle


class TestRectMethods(unittest.TestCase):
    """rect tests"""

    def test_inherits(self):
        """test rectangle.Rectangle"""
        pass

    def test_no_args(self):
        with self.assertRaises(TypeError):
            rectangle.Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1)

    def test_two_args(self):
        r1 = rectangle.Rectangle(10, 2)
        r2 = rectangle.Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = rectangle.Rectangle(2, 2, 4)
        r2 = rectangle.Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = rectangle.Rectangle(1, 2, 3, 4)
        r2 = rectangle.Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(7, rectangle.Rectangle(10, 2, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            rectangle.Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(rectangle.Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(rectangle.Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(rectangle.Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(rectangle.Rectangle(5, 5, 0, 0, 1).__y)

    def test_constructor(self):
        """test rectangle.Rectangle"""

        rect = rectangle.Rectangle(5, 3, 7, 2, 99)

        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 99)

    def test_validator(self):
        """test rectangle.Rectangle"""

        pass

    def test_area(self):
        """test rectangle.Rectangle"""

        # small area
        r = rectangle.Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

        # large area
        r = rectangle.Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

        # extra area
        r = rectangle.Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_update_args(self):
        """test rectangle.Rectangle"""

        rect = rectangle.Rectangle(5, 5)

        # check for function
        self.assertTrue('update' in dir(rect))

        # test id update
        rect.update(89)
        self.assertEqual(rect.id, 89)

        # test width update
        rect.update(89, 2)
        self.assertEqual(rect.width, 2)

        # test height upadte
        rect.update(89, 2, 3)
        self.assertEqual(rect.height, 3)

        # test x update
        rect.update(89, 2, 3, 4)
        self.assertEqual(rect.x, 4)

        # test y update
        rect.update(89, 2, 3, 4, 2)
        self.assertEqual(rect.y, 2)

    def test_update_kwargs(self):
        """test rectangle.Rectangle"""

        rect = rectangle.Rectangle(1, 1, 0, 0, 1)

        # test id update
        rect.update(id=89)
        self.assertEqual(rect.id, 89)

        # test width update
        rect.update(width=10)
        self.assertEqual(rect.width, 10)

        # test height update
        rect.update(height=10)
        self.assertEqual(rect.height, 10)

        # test x update
        rect.update(x=5)
        self.assertEqual(rect.x, 5)

        # test y update
        rect.update(y=5)
        self.assertEqual(rect.y, 5)

    def test_to_dict(self):
        """test rectangle.Rectangle"""

        pass

if __name__ == '__main__':
    unittest.main()
