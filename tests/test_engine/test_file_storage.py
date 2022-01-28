#!/usr/bin/env python3
"""unittest file for the file_storage.py module"""
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import unittest

storage = FileStorage()


class TestFileStorage(unittest.TestCase):
    """class to test the FileStorage class"""
    def setUp(self):
        self.base = BaseModel()
        self.user = User()
        self.base_key = f"{type(self.base).__name__}.{self.base.id}"
        self.user_key = f"{type(self.user).__name__}.{self.user.id}"

    def tearDown(self):
        del storage.all()[self.base_key]
        del storage.all()[self.user_key]

    def testfilepathisprivate(self):
        with self.assertRaises(AttributeError):
            path = storage.__file_path

    def testobjectstoreisprivate(self):
        with self.assertRaises(AttributeError):
            objects = storage.__objects

    def testall(self):
        """tests the all() method"""
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())

    def testnew(self):
        """tests the new() method"""
        base_obj = BaseModel()
        user_obj = User()
        storage.new(base_obj)
        storage.new(user_obj)
        base_obj_key = f"{type(base_obj).__name__}.{base_obj.id}"
        user_obj_key = f"{type(user_obj).__name__}.{user_obj.id}"
        self.assertIn(base_obj_key, storage.all())
        self.assertIn(user_obj_key, storage.all())
        del storage.all()[base_obj_key]
        del storage.all()[user_obj_key]

    def testsave(self):
        """tests the save() method"""
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())
        storage.reload()
        self.assertNotIn(self.base_key, storage.all())
        self.assertNotIn(self.user_key, storage.all())
        storage.new(self.base)
        storage.new(self.user)
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())
        storage.save()
        storage.reload()
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())

    def testreload(self):
        """tests the reload() method"""
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())
        storage.reload()
        self.assertNotIn(self.base_key, storage.all())
        self.assertNotIn(self.user_key, storage.all())
        storage.new(self.base)
        storage.new(self.user)
