#!/usr/bin/python3
"""Defines Unittests for model rectangle.py"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 10, 2, 3, 1)

    def test_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, -10, 2, 3, 1)

    def test_x_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, -2, 3, 1)

    def test_y_validation(self):
        with self.assertRaises(ValueError):
            r = Rectangle(5, 10, 2, -3, 1)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2, 1, 1)
        output = " ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), output)

    def test_update(self):
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(2, 6, 12, 4, 5)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)
        list_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), list_dict)

if __name__ == '__main__':
    unittest.main()
