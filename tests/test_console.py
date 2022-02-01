#!/usr/bin/env python3
"""unittest test file for compile.py module"""
import unittest
import os
from io import StringIO
from unittest.mock import patch
from sys import path as sys_path
script_dir = os.path.dirname(__file__)
sys_path.append(os.path.join(script_dir, ".."))
from models import storage  # noqa: E402
from models.base_model import BaseModel  # noqa: E402
from models.user import User   # noqa: E402
from models.state import State  # noqa: E402
from models.city import City  # noqa: E402
from models.place import Place  # noqa: E402
from models.amenity import Amenity  # noqa: E402
from models.review import Review  # noqa: E402
from console import HBNBCommand  # noqa: E402


class TestHelp(unittest.TestCase):
    """ tests the help command"""
    def test_help_create(self):
        """ test correct help output for create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        create_doc = HBNBCommand().do_create.__doc__
        self.assertEqual(f.getvalue()[:-1], create_doc)

    def test_help_show(self):
        """test correct help output for show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        show_doc = HBNBCommand().do_show.__doc__
        self.assertEqual(f.getvalue()[:-1], show_doc)

    def test_help_destroy(self):
        """ test correct help output for destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        destroy_doc = HBNBCommand().do_destroy.__doc__
        self.assertEqual(f.getvalue()[:-1], destroy_doc)

    def test_help_all(self):
        """ test correct help output for all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        all_doc = HBNBCommand().do_all.__doc__
        self.assertEqual(f.getvalue()[:-1], all_doc)

    def test_help_update(self):
        """ test correct help output for update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        update_doc = HBNBCommand().do_update.__doc__
        self.assertEqual(f.getvalue()[:-1], update_doc)

    def test_help_quit(self):
        """test correct help output for quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        quit_doc = HBNBCommand().do_quit.__doc__
        self.assertEqual(f.getvalue()[:-1], quit_doc)

    def test_help_EOF(self):
        """test correct help output for EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        EOF_doc = HBNBCommand().do_EOF.__doc__
        self.assertEqual(f.getvalue()[:-1], EOF_doc)


class TestMiscellaneousCommands(unittest.TestCase):
    '''test EOF, quit commands and emptyline + Enter'''

    def test_empty_line_enter(self):
        """test the empty line + enter command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        self.assertEqual(f.getvalue(), "")

    def test_quit_command(self):
        ''' test quit command'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertRaises(SystemExit, HBNBCommand().onecmd, "quit")

    def test_EOF_command(self):
        ''' test EOF command'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertRaises(SystemExit, HBNBCommand().onecmd, "EOF")


class TestCreateCommand(unittest.TestCase):
    '''test the create command'''

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_without_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        expected = "** class name missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_create_with_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        id = f.getvalue()[:-1]
        key = f"BaseModel.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_User_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()[:-1]
        key = f"User.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_City_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
        id = f.getvalue()[:-1]
        key = f"City.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_Place_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        id = f.getvalue()[:-1]
        key = f"Place.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_State_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
        id = f.getvalue()[:-1]
        key = f"State.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_Amenity_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
        id = f.getvalue()[:-1]
        key = f"Amenity.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_Review_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
        id = f.getvalue()[:-1]
        key = f"Review.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_BaseModel_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
        id = f.getvalue()[:-1]
        key = f"BaseModel.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_User_model_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
        id = f.getvalue()[:-1]
        key = f"User.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_City_model_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
        id = f.getvalue()[:-1]
        key = f"City.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_Place_model_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
        id = f.getvalue()[:-1]
        key = f"Place.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_State_model_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
        id = f.getvalue()[:-1]
        key = f"State.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_Amenity_model_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
        id = f.getvalue()[:-1]
        key = f"Amenity.{id}"
        self.assertIn(key, storage.all().keys())

    def test_create_with_Review_model_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
        id = f.getvalue()[:-1]
        key = f"Review.{id}"
        self.assertIn(key, storage.all().keys())


class TestShowCommand(unittest.TestCase):
    ''' test the show command '''

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_show_without_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        expected = "** class name missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_show_without_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel")
        expected = "** instance id missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_show_with_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 7585966")
        expected = "** no instance found **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_show_with_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {id}")
        key = f"BaseModel.{id}"
        obj = BaseModel(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show User {id}")
        key = f"User.{id}"
        obj = User(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_State(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show State {id}")
        key = f"State.{id}"
        obj = State(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_Place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Place {id}")
        key = f"Place.{id}"
        obj = Place(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_Amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Amenity {id}")
        key = f"Amenity.{id}"
        obj = Amenity(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_Review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show Review {id}")
        key = f"Review.{id}"
        obj = Review(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_without_id_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show()")
        expected = "** instance id missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_show_with_invalid_id_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show(7585966)")
        expected = "** no instance found **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_show_with_BaseModel_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({id})")
        key = f"BaseModel.{id}"
        obj = BaseModel(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_User_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({id})")
        key = f"User.{id}"
        obj = User(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_State_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({id})")
        key = f"State.{id}"
        obj = State(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_Place_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({id})")
        key = f"Place.{id}"
        obj = Place(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_Amenity_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({id})")
        key = f"Amenity.{id}"
        obj = Amenity(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))

    def test_show_with_Review_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            id = f.getvalue()[:-1]
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({id})")
        key = f"Review.{id}"
        obj = Review(**storage.all()[key])
        self.assertEqual(f.getvalue()[:-1], str(obj))


class TestDestroyCommand(unittest.TestCase):
    '''test the destroy command'''

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_destroy_without_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        expected = "** class name missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_destroy_without_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
        expected = "** instance id missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_destroy_with_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel model")
        expected = "** no instance found **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_destroy_with_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            id = f.getvalue()[:-1]
        key = f"BaseModel.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy BaseModel {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            id = f.getvalue()[:-1]
        key = f"User.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy User {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_Place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            id = f.getvalue()[:-1]
        key = f"Place.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy Place {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_State(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            id = f.getvalue()[:-1]
        key = f"State.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy State {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_City(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            id = f.getvalue()[:-1]
        key = f"City.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy City {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_Amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            id = f.getvalue()[:-1]
        key = f"Amenity.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy Amenity {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_Review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            id = f.getvalue()[:-1]
        key = f"Review.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"destroy Review {id}")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_without_id_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy()")
        expected = "** instance id missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_destroy_with_invalid_id_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy(model)")
        expected = "** no instance found **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_destroy_with_BaseModel_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            id = f.getvalue()[:-1]
        key = f"BaseModel.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"BaseModel.destroy({id})")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_User_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            id = f.getvalue()[:-1]
        key = f"User.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"User.destroy({id})")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_Place_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            id = f.getvalue()[:-1]
        key = f"Place.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"Place.destroy({id})")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_State_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            id = f.getvalue()[:-1]
        key = f"State.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"State.destroy({id})")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_City_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            id = f.getvalue()[:-1]
        key = f"City.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"City.destroy({id})")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_Amenity_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            id = f.getvalue()[:-1]
        key = f"Amenity.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"Amenity.destroy({id})")
        self.assertNotIn(key, storage.all().keys())

    def test_destroy_with_Review_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            id = f.getvalue()[:-1]
        key = f"Review.{id}"
        self.assertIn(key, storage.all().keys())
        HBNBCommand().onecmd(f"Review.destroy({id})")
        self.assertNotIn(key, storage.all().keys())


class TestAllCommand(unittest.TestCase):
    """Tests the all command"""

    def setUp(self):
        self.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
        }
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create State")
            HBNBCommand().onecmd("create City")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("create Amenity")
            HBNBCommand().onecmd("create Review")
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_without_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        expected = []
        for key, value in storage.all().items():
            obj_class = self.classes[key.split(".")[0]]
            obj = obj_class(**value)
            expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_BaseModel(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        expected = []
        for key, value in storage.all().items():
            if "BaseModel" in key:
                obj = BaseModel(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_User(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
        expected = []
        for key, value in storage.all().items():
            if "User" in key:
                obj = User(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_Place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Place")
        expected = []
        for key, value in storage.all().items():
            if "Place" in key:
                obj = Place(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_State(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
        expected = []
        for key, value in storage.all().items():
            if "State" in key:
                obj = State(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_City(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all City")
        expected = []
        for key, value in storage.all().items():
            if "City" in key:
                obj = City(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_Amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Amenity")
        expected = []
        for key, value in storage.all().items():
            if "Amenity" in key:
                obj = Amenity(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_Review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all Review")
        expected = []
        for key, value in storage.all().items():
            if "Review" in key:
                obj = Review(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_BaseModel_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        expected = []
        for key, value in storage.all().items():
            if "BaseModel" in key:
                obj = BaseModel(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_User_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
        expected = []
        for key, value in storage.all().items():
            if "User" in key:
                obj = User(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_Place_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        expected = []
        for key, value in storage.all().items():
            if "Place" in key:
                obj = Place(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_State_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        expected = []
        for key, value in storage.all().items():
            if "State" in key:
                obj = State(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_City_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        expected = []
        for key, value in storage.all().items():
            if "City" in key:
                obj = City(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_Amenity_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        expected = []
        for key, value in storage.all().items():
            if "Amenity" in key:
                obj = Amenity(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))

    def test_all_with_Review_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        expected = []
        for key, value in storage.all().items():
            if "Review" in key:
                obj = Review(**value)
                expected.append(str(obj))
        self.assertEqual(f.getvalue()[:-1], str(expected))


class TestUpdateCommand(unittest.TestCase):
    '''test the update command'''

    def setUp(self):
        self.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
        }
        self.base = BaseModel()
        self.user = User()
        self.place = Place()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.review = Review()

        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_update_without_classname(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        expected = "** class name missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_without_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel")
        expected = "** instance id missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_with_invalid_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel an_id")
        expected = "** no instance found **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_without_attr_name(self):
        id = self.base.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update BaseModel {id}")
        expected = "** attribute name missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_without_attr_value(self):
        id = self.user.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update User {id} name")
        expected = "** value missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_BaseModel(self):
        id = self.base.id
        HBNBCommand().onecmd(f'update BaseModel {id} name "Alx"')
        key = f"BaseModel.{id}"
        with self.assertRaises(AttributeError):
            name = self.base.name
        self.base = BaseModel(**storage.all()[key])
        self.assertEqual(self.base.name, "Alx")

    def test_update_User(self):
        id = self.user.id
        self.assertNotEqual(self.user.email, "we@alx.com")
        HBNBCommand().onecmd(f'update User {id} email "we@alx.com"')
        key = f"User.{id}"
        self.user = User(**storage.all()[key])
        self.assertEqual(self.user.email, 'we@alx.com')

    def test_update_Place(self):
        id = self.place.id
        self.assertNotEqual(self.place.latitude, 45.5)
        HBNBCommand().onecmd(f'update Place {id} latitude 45.5')
        key = f"Place.{id}"
        self.place = Place(**storage.all()[key])
        self.assertEqual(self.place.latitude, 45.5)

    def test_update_State(self):
        id = self.state.id
        self.assertNotEqual(self.state.name, "Ibadan")
        HBNBCommand().onecmd(f'update State {id} name "Ibadan"')
        key = f"State.{id}"
        self.state = State(**storage.all()[key])
        self.assertEqual(self.state.name, "Ibadan")

    def test_update_City(self):
        id = self.city.id
        self.assertNotEqual(self.city.state_id, self.state.id)
        HBNBCommand().onecmd(f'update City {id} state_id {self.state.id}')
        key = f"City.{id}"
        self.city = City(**storage.all()[key])
        self.assertEqual(self.city.state_id, self.state.id)

    def test_update_Amenity(self):
        id = self.amenity.id
        self.assertNotEqual(self.amenity.name, "Internet")
        HBNBCommand().onecmd(f'update Amenity {id} name Internet')
        key = f"Amenity.{id}"
        self.amenity = Amenity(**storage.all()[key])
        self.assertEqual(self.amenity.name, "Internet")

    def test_update_Review(self):
        id = self.review.id
        self.assertNotEqual(self.review.user_id, self.user.id)
        HBNBCommand().onecmd(f'update Review {id} user_id {self.user.id}')
        key = f"Review.{id}"
        self.review = Review(**storage.all()[key])
        self.assertEqual(self.review.user_id, self.user.id)

    def test_update_without_id_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update()")
        expected = "** instance id missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_with_invalid_id_alternate(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.update(an_id)")
        expected = "** no instance found **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_without_attr_name_alternate(self):
        id = self.base.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({id})")
        expected = "** attribute name missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_without_attr_value_alternate(self):
        id = self.user.id
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({id}, name)")
        expected = "** value missing **\n"
        self.assertEqual(f.getvalue(), expected)

    def test_update_BaseModel_alternate(self):
        id = self.base.id
        HBNBCommand().onecmd(f'BaseModel.update({id}, name, "Alx")')
        key = f"BaseModel.{id}"
        with self.assertRaises(AttributeError):
            name = self.base.name
        self.base = BaseModel(**storage.all()[key])
        self.assertEqual(self.base.name, "Alx")

    def test_update_User_alternate(self):
        id = self.user.id
        self.assertNotEqual(self.user.email, "we@alx.com")
        HBNBCommand().onecmd(f'User.update({id}, email, "we@alx.com")')
        key = f"User.{id}"
        self.user = User(**storage.all()[key])
        self.assertEqual(self.user.email, 'we@alx.com')

    def test_update_Place_alternate(self):
        id = self.place.id
        self.assertNotEqual(self.place.latitude, 45.5)
        HBNBCommand().onecmd(f'Place.update({id}, latitude, 45.5)')
        key = f"Place.{id}"
        self.place = Place(**storage.all()[key])
        self.assertEqual(self.place.latitude, 45.5)

    def test_update_State_alternate(self):
        id = self.state.id
        self.assertNotEqual(self.state.name, "Ibadan")
        HBNBCommand().onecmd(f'State.update({id}, name, "Ibadan")')
        key = f"State.{id}"
        self.state = State(**storage.all()[key])
        self.assertEqual(self.state.name, "Ibadan")

    def test_update_City_alternate(self):
        id = self.city.id
        self.assertNotEqual(self.city.state_id, self.state.id)
        HBNBCommand().onecmd(f'City.update({id}, state_id, {self.state.id})')
        key = f"City.{id}"
        self.city = City(**storage.all()[key])
        self.assertEqual(self.city.state_id, self.state.id)

    def test_update_Amenity_alternate(self):
        id = self.amenity.id
        self.assertNotEqual(self.amenity.name, "Internet")
        HBNBCommand().onecmd(f'Amenity.update({id}, name, Internet)')
        key = f"Amenity.{id}"
        self.amenity = Amenity(**storage.all()[key])
        self.assertEqual(self.amenity.name, "Internet")

    def test_update_Review_alternate(self):
        id = self.review.id
        self.assertNotEqual(self.review.user_id, self.user.id)
        HBNBCommand().onecmd(f'Review.update({id}, user_id, {self.user.id})')
        key = f"Review.{id}"
        self.review = Review(**storage.all()[key])
        self.assertEqual(self.review.user_id, self.user.id)

    def test_update_with_dictionary(self):
        id = self.place.id
        self.assertNotEqual(self.place.city_id, self.city.id)
        self.assertNotEqual(self.place.user_id, self.user.id)
        self.assertNotEqual(self.place.longitude, 100.0)
        self.assertNotEqual(self.place.latitude, 45.5)
        city = self.city.id
        user = self.user.id
        HBNBCommand().onecmd(
                            f'Place.update({id}, {{\
                             city_id:{city},\
                             user_id:{user},\
                             longitude: 100.0,\
                             latitude:45.5\
                             }})'
                            )
        key = f"Place.{id}"
        self.place = Place(**storage.all()[key])
        self.assertEqual(self.place.latitude, 45.5)


if __name__ == "__main__":
    unittest.main()
