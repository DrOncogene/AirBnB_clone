#!/usr/bin/python3
""" Test for amenity class """

import models
import unittest
from models.amenity import Amenity
"""Test class Amenity"""


class TestState(unittest.TestCase):
    """Simple test case for State class"""
    def test_attr(self):
        attr = hasattr(Amenity, 'name')
        self.assertEqual(attr, True)

    def test_type(self):
        """Test the type of State public attr"""
        type_ = type(Amenity.name).__name__
        self.assertEqual(type_, "str")


if __name__ == "__main__":
    unittest.main()
