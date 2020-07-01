#!/usr/bin/python3
"""User's module"""

from models.base_model import BaseModel


class User(BaseModel):
    """user's information"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
