#!/usr/bin/env python3
"""module that defines the base class for creating unique
identifiers for objects"""
import uuid
from models import storage
from datetime import datetime
from models import storage


class BaseModel:
    """class to define the BaseModel, mainly to generate
    unique ids"""
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            if k == "created_at":
                self.created_at = datetime.fromisoformat(v)
            elif k == "updated_at":
                self.updated_at = datetime.fromisoformat(v)
            elif k == "id":
                self.id = v
            elif k != "__class__":
                self.__dict__[k] = v
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self: object) -> dict:
        """string representation of the obj"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the updated_at attr of self"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self: object) -> dict:
        """returns a dict of attributes of the current instance"""
        attr_dict = self.__dict__.copy()
        attr_dict["__class__"] = self.__class__.__name__
        attr_dict["created_at"] = self.created_at.isoformat()
        attr_dict["updated_at"] = self.updated_at.isoformat()
        return attr_dict
