#!/usr/bin/python3
"""City class that inherit from Basemodel"""

from models.base_model import BaseModel


class City(BaseModel):
    """ City class """

    state_id = ""
    name = ""
