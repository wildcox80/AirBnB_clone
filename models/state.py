#!/usr/bin/python3
"""State Module"""
from models.base_model import BaseModel


class State(BaseModel):
    """State in a Country"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State constructor"""
        super().__init__(*args, **kwargs)
