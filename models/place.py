#!/usr/bin/python3
"""Place Model"""
from models.base_model import BaseModel


class Place(BaseModel):
    """structure of the db"""
    city_id = ""  # City.id format
    user_id = ""  # User.id format
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""  # Amenity.id format

    def __init__(self, *args, **kwargs):
        """Place class constructor"""
        super().__init__(*args, **kwargs)
