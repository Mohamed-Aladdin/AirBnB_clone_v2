#!/usr/bin/python3
"""Console Module Tests"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
from os import getenv


class TestConsole(unittest.TestCase):
    """test the console"""
    console = HBNBCommand()

    def setUp(self):
        """setup for the test"""
        pass

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("file.json")
        except Exception:
            pass
        
    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0, 'fix Pep8')
        
    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db", "Using db")
    def test_create(self):
        print(getenv("HBNB_TYPE_STORAGE") != "db")
        """Test create command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(f.getvalue() is not None)
            
if __name__ == "__main__":
    unittest.main()