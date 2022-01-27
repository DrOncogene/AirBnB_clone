#!/usr/bin/env python3
"""Module to define a serialization/deserialization engine
that saves objects to a file"""

import json
from os import path as os_path


class FileStorage:
    """class that defines a file storage engine
    for JSON serialization"""
    __file_path = "file.json"
    __objects = {}

    def all(self) -> dict:
        """returns __objects"""
        return FileStorage.__objects

    def new(self, obj) -> None:
        """sets a new obj in __objects"""
        FileStorage.__objects[
            f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """serializes __objects to a JSON file in __file_path"""
        json_str = json.dumps(FileStorage.__objects, indent=2)
        with open(f"{FileStorage.__file_path}", "w") as f:
            f.write(json_str)

    def reload(self):
        """deserializes a json file at __file_path and save
        it in __objects"""
        if os_path.exists(FileStorage.__file_path):
            with open(f"{FileStorage.__file_path}", "r") as f:
                json_str = f.read()
                if len(json_str) == 0:
                    return
                FileStorage.__objects = json.loads(json_str)
