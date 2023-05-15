#!/usr/bin/python
""" holds User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Rep of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """init user"""
        super().__init__(*args, **kwargs)
