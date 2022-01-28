#!/usr/bin/python3
"""Test class State"""

import models
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Simple test case for State class"""
    def test_attr(self):
        attr = hasattr(State, 'name')
        self.assertEqual(attr, True)

    def test_type(self):
        """Test the type of State public attr"""
        type_ = type(State.name).__name__
        self.assertEqual(type_, "str")


if __name__ == "__main__":
    unittest.main()
