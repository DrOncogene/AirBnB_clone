#!/usr/bin/python3
""" Test suits for class User"""

import models
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ simple test case model """

    def test_attr(self):
        """
        Tests for public class attrubute
        """
        attr_list = ['email',
                     'first_name',
                     'last_name',
                     'password']
        is_attr = False
        for attri in attr_list:
            is_attr = hasattr(User, attri)
            if not is_attr:
                break
        self.assertEqual(is_attr, True)

    def test_type_attr(self):
        """
        Test the type of state attribute
        """
        type_email = type(User.email).__name__
        type_first_name = type(User.first_name).__name__
        type_last_name = type(User.last_name).__name__
        type_password = type(User.password).__name__

        self.assertEqual(type_password, "str")
        self.assertEqual(type_email, "str")
        self.assertEqual(type_first_name, "str")
        self.assertEqual(type_last_name, "str")


if __name__ == '__main__':
    unittest.main()
