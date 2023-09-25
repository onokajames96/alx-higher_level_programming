#!/usr/bin/python3
""""""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """
    def test_init_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_empty_to_json_string(self):
        json_string = Base.to_json_string([])

