#!/usr/bin/python3
"""Review class inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """simple Review model"""

    place_id = ""
    user_id = ""
    text = ""
