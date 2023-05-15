#!/usr/bin/python
""" holds State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """Rep of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """init state"""
        super().__init__(*args, **kwargs)
