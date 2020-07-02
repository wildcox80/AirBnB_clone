#!/usr/bin/python3
"""Module Amenity """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity to BaseModel """
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity constructor"""
        super().__init__(*args, **kwargs)
