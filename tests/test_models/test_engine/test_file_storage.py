#!/usr/bin/env python3
"""unittest file for the file_storage.py module"""
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
import uuid

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

    def test_file_path_is_private(self):
        """checks that storage filepath is private"""
        with self.assertRaises(AttributeError):
            path = storage.__file_path

    def test_objectstore_is_private(self):
        """checks that storage temp objects store dict is private"""
        with self.assertRaises(AttributeError):
            objects = storage.__objects

    def test_all(self):
        """tests the all() method"""
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())

    def test_new(self):
        """tests the new() method"""
        base_obj_dict = {
            "id": uuid.uuid4(),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }
        user_obj_dict = {
            "id": uuid.uuid4(),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "email": 'user@alx.com'
        }
        base_obj = BaseModel(**base_obj_dict)
        user_obj = User(**user_obj_dict)
        base_obj_key = f"{type(base_obj).__name__}.{base_obj.id}"
        user_obj_key = f"{type(user_obj).__name__}.{user_obj.id}"
        self.assertNotIn(base_obj_key, storage.all())
        self.assertNotIn(user_obj_key, storage.all())
        storage.new(base_obj)
        storage.new(user_obj)
        self.assertIn(base_obj_key, storage.all())
        self.assertIn(user_obj_key, storage.all())
        del storage.all()[base_obj_key]
        del storage.all()[user_obj_key]

    def test_save(self):
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

    def test_reload(self):
        """tests the reload() method"""
        self.assertIn(self.base_key, storage.all())
        self.assertIn(self.user_key, storage.all())
        storage.reload()
        self.assertNotIn(self.base_key, storage.all())
        self.assertNotIn(self.user_key, storage.all())
        storage.new(self.base)
        storage.new(self.user)
