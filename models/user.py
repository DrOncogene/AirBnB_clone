#!usr/bin/pyhton3
""" A class User that inherits from BaseModel """


from models.base_model import BaseModel


class User(BaseModel):
    """ Simple user class model """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
