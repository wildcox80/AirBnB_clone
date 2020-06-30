#!/usr/bin/python3
""" Modules for Class """

import datetime
import uuid
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Class Base Model"""

    def __init__(self, *args, **kwargs):
        """ Constructor Method """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

        else:
            for attr_name, attr in kwargs.items():
                if attr_name == "created_at" or attr_name == "updated_at":
                    attr = datetime.strptime(attr, "%Y-%m-%dT%H:%M:%S.%f")
                if attr_name != "__class__":
                    setattr(self, attr_name, attr)

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
