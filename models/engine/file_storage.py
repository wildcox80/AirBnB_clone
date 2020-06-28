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

    