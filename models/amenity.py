#!/usr/bin/python
""" holds Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Rep of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """init Amenity"""
        super().__init__(*args, **kwargs)
