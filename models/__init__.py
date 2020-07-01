#!/usr/bin/python3
"""
creating a unique FileStorage instance
for the application.
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State


storage = FileStorage()

# calling reload() method on this var (task5).
storage.reload()
