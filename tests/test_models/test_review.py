#!/usr/bin/python3
"""Test class Review"""

import models
import unittest
from models.review import Review


class Test_review(unittest.TestCase):
    """Simple test model"""

    def test_attr(self):
        """Test class attrbute"""
        is_attr = False
        list_ = [
            'place_id',
            'user_id',
            'text'
            ]
        for key in list_:
            attr = hasattr(Review, key)
            if not attr:
                break
        self.assertEqual(attr, True)

    def test_type_str(self):
        """Test type of class attribute"""

        splace_id = type(Review.place_id).__name__
        suser_id = type(Review.user_id).__name__
        stext = type(Review.text).__name__

        self.assertEqual(splace_id, 'str')
        self.assertEqual(suser_id, 'str')
        self.assertEqual(stext, 'str')


if __name__ == "__main__":
    unittest.main()
