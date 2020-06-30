#!/usr/bin/python3
""" Create Class FileStorage """
import json
import models

class FileStorage:
    """ Define class FileStorage """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Return all __object of the dictionary """

        return self.__objects

    def new(self, obj):
        """ Return obj in object format """

    if obj:
        key = "{}.{}".format(obj.__class__.__name__, obj.id)


    def save(self):
        """serializes __objects to __file_path"""
        obj_dict = {}
        for object_id, ob in self.__objects.items():
            obj_dict[object_id] = ob.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)


    def reload(self):
        """deserializes __objects from __file_path"""
        try:
            with open(self.__file_path, encoding="UTF-8") as f:
                obj = json.load(f)
            for obj_id, dictionary in obj.items():
                val = models.cls_dict[dictionary['__class__']](**dictionary)
                self.__objects[obj_id] = val
        except FileNotFoundError:
            pass

