#!/usr/bin/python3
"""Test case for class City"""

import models
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Simple test model for class City"""

    def test_attr(self):
        """Test for attribute"""
        attr_list = ['state_id', 'name']
        is_attr = False
        for attri in attr_list:
            is_attr = hasattr(City, attri)
            if not is_attr:
                break
        self.assertEqual(is_attr, True)

    def test_type_state_id(self):
        """Test the type of state id attribute"""
        type_id = type(City.state_id).__name__
        self.assertEqual(type_id, "str")

    def test_type_name(self):
        """Test the type of name attribute"""
        type_ = type(City.name).__name__
        self.assertEqual(type_, "str")


if __name__ == "__main__":
    unittest.main()
