#!/usr/bin/python
""" holds Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Rep of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """init Review"""
        super().__init__(*args, **kwargs)
