#!/usr/bin/python3
"""Unittest for Console"""

import unittest
import console
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Console Unittest"""

    def create(self):
        """ Create instance command line """
        return HBNBCommand()

    def test_quit(self, server=None):
        """Creates HBNBCommand"""
        con = self.create()
        self.assertTrue(con.onecmd("quit"))

    def test_EOF(self):
        """Tests the quit command"""
        con = self.create()
        self.assertTrue(con.onecmd("EOF"))


if __name__ == '__main__':
    unittest.main()
