# /usr/bin/python3
""" Modules for Class """
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Class Base Model"""

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ String Method """
        return("[{}] ({}) {}"
               .format(type(self).__class__, self.id, self.__dict__))

     def save(self):
         """Save instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a Dictionary """
        new_dict = self.__dict__.copy()
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return(new_dict)
