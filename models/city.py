#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city of the place"""
    state_id = ""  # Could be state.id format
    name = ""

    def __init__(self, *args, **kwargs):
        """City class constructor"""
        super().__init__(*args, **kwargs)
