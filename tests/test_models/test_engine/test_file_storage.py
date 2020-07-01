#!/usr/bin/python3
"""File Storage Unit Tests"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import models
import os
import sys
import pep8
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Test cases for class FileStorage
    """
    def test_docstring(self):
        """Checks if docstring exist"""

        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""

        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """Sets up the testing environment to not change the
        previous file storage
        """

        self.file_path = models.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, 'test_storage')

    def tearDown(self):
        """ Removes the JSON file after test cases run """

        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists('test_storage'):
            os.rename('test_storage', self.file_path)

    def test_instantiation(self):
        """Tests for proper instantiation"""

        temp_storage = FileStorage()
        self.assertIsInstance(temp_storage, FileStorage)

    def test_saves_new_instance(self):
        """Tests if file is being created """

        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_all(self):
        """Tests the all method"""

        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        self.assertIsNotNone(temp_dict)
        self.assertEqual(type(temp_dict), dict)


if __name__ == '__main__':
    unittest.main()
