#!/usr/bin/python
""" holds City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Rep of city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initi city"""
        super().__init__(*args, **kwargs)
