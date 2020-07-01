#!/usr/bin/python3
"""City Module"""
from models.base_model import BaseModel


class City(BaseModel):
    """the city of the place"""
    state_id = ""  # Could be state.id format
    name = ""
