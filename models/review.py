#!/usr/bin/python3
"""Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """this class save reviews"""
    place_id = ""  # Place.id format
    user_id = ""  # User.id format
    text = ""

    def __init__(self, *args, **kwargs):
        """Review class constructor"""
        super().__init__(*args, **kwargs)
