#!/usr/bin/env python3
"""unittest file for the file_storage.py module"""
from datetime import datetime
import unittest
import uuid
import os
from sys import path as sys_path
script_dir = os.path.dirname(__file__)
sys_path.append(os.path.join(script_dir, "../../.."))
from models import storage  # noqa: E402
from models.base_model import BaseModel  # noqa: E402
from models.user import User   # noqa: E402


class TestFileStorage(unittest.TestCase):
    """class to test the FileStorage class"""

    def setUp(self):
        self.base, self.user = BaseModel(), User()
        self.base_key = f"BaseModel.{self.base.id}"
        self.user_key = f"User.{self.user.id}"

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

        base_obj = BaseModel(**{
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "update_at": datetime.now().isoformat()
        })
        user_obj = User(**{
            "id": str(uuid.uuid4()),
            "created_at": datetime.now().isoformat(),
            "update_at": datetime.now().isoformat(),
            "first_name": "Haliborton",
            "age": 50
        })
        base_obj_key = f"BaseModel.{base_obj.id}"
        user_obj_key = f"User.{user_obj.id}"
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


if __name__ == "__main__":
    unittest.main()
