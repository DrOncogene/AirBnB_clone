#!/usr/bin/env python3
"""the program that serves as the entry point to the command
line interpreter for the Airbnb console"""
import cmd

import sys
import json
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class the defines the console object"""
    prompt = "(hbnb) "
    # all available classes
    _classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
    }
    _types = {
        'number_rooms': int,
        'number_bathrooms': int,
        'max_guest': int,
        'price_by_night': int,
        'latitude': float,
        'longitude': float,
    }

    def do_EOF(self, arg: str) -> None:
        """Exits the interpreter. USAGE: EOF\n"""
        sys.exit(0)

    def do_quit(self, arg: str) -> None:
        """Quit command to exit the program\n"""
        sys.exit(0)

    def emptyline(self):
        """overrides the emptyline method of cmd"""
        return

    def default(self, line: str) -> None:
        # match the syntax 'class.command(args)'
        pattern = re.compile(r'(\w+)\.(\w+)\(([\S ]*)\)')
        res = pattern.findall(line) # returns a list of tuples

        # check if pattern found
        if len(res) < 1 or len(res[0]) < 3:
            # if not found call the cmd default and return
            super().default(line)
            return
        res = res[0] # set result to first tuple in the list
        class_name = res[0]
        command = res[1]
        args = res[2]
        if command == "all":
            # run a one liner with classname
            self.onecmd(f"{command} {class_name}")
            return
        elif command == "count":
            # call do_all with count set to true
            count = self.do_all(f"{class_name}", count=True)
            print(count)
            return
        else:
            # check if args is dict
            if "{" in args and "}" in args:
                # call the dict version of update method
                self.dict_update(class_name, args)
                return

            self.onecmd(f"{command} {class_name} {args}")
            return
        super().default(line)

    def do_create(self, arg: str) -> None:
        """creates a new instance of a class passed as argument
		USAGE: create <class_name>"""
        args = parse_args(arg)
        if validate_args(args, 1) == -1:
            return
        cls = args[0]
        args = check_params(args[1:])
        new = HBNBCommand._classes[cls]()
        for arg in args:
            attr, value = arg.split('=')
            if attr in dir(new):
                attr_t = self._types[attr] if attr in self._types else None
                new.__dict__[attr] = ( value if attr_t is None
                               else attr_t(value))
        storage.save()
        print(new.id)

    def do_show(self, arg: str) -> None:
        """prints the str representation of an instance
		USAGE: show <classname> <id>"""
        args = parse_args(arg)
        if validate_args(args, 2) == -1:
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            obj = storage.all()[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg: str) -> None:
        """deletes a given instance from storage
		USAGE: destroy <classname> <id>"""
        args = parse_args(arg)
        if validate_args(args, 2) == -1:
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg: str, count=False):
        """prints all instances
		USAGE: all <classname> or all"""
        args = parse_args(arg)
        obj_list = []
        if len(args) > 0:
            if validate_args(args, 1) == -1:
                return
            for key, obj in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj))
            if count:
                return len(obj_list)
            print(obj_list)
            return
        for key, obj in storage.all().items():
            obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg: str) -> None:
        """update the given attribute of a given object.
		USAGE: update <class name> <id> <attr name> '<attr value>'"""
        args = parse_args(arg)
        if validate_args(args, 4) == -1:
            return
        class_name, id = args[0], args[1]
        key = f"{class_name}.{id}"
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr, value = args[2], args[3]
        obj = storage.all()[key]
        if attr in dir(obj):
            attr_type = type(getattr(obj, attr))
            obj.__dict__[attr] = attr_type(value)

        obj.save()

    def dict_update(self, class_name: str, arg: str) -> None:
        """resolves the dict representation of update command
        if <classname>.update(<id>, <dict>) sytax is used"""

        # match the id and dict pattern i.e. 'id, update_dict'
        pattern = re.compile(r'([\w\-]+),\s*(\{.*\})')
        res = pattern.findall(arg)
        if len(res) < 1:
            self.onecmd(f"update {class_name} {arg}")
            return
        id = res[0][0]
        obj_dict = eval(res[0][1])
        for key, value in obj_dict.items():
            self.onecmd(f"update {class_name} {id} {key} {value}")


def parse_args(arg: str, delim=" ") -> list:
    """processes the command string and returns a
    list of command-line args"""

    # return empty list if arg string is empty
    if arg == "":
        return []

    # split args string by delim (space is default)
    args = arg.split(delim)
    i = 0
    while i < len(args):
        curr = args[i].strip(",") # removes commas

        # try to reconstruct quoted args that contains spaces
        # which would have been splitted by .split()
        if curr[0] == '"' and curr[-1] != '"':
            if i == len(args) - 1:
                args[i] = curr.replace('"', '')
                break
            for j in range(i + 1, len(args)):
                next = args[j]
                if next[-1] == '"':
                    found = 1
                    break
            full = curr
            for k in range(i + 1, j + 1):
                full += f" {args[k]}"
            full = full.strip('"')
            full = full.strip("'")
            args.insert(i, full)
            args_copy = args.copy()
            for k in range(i + 1, j + 2):
                args.pop(args.index(args_copy[k]))
        else:
            if curr[0] == '"':
                curr = curr.strip('"')
            args[i] = curr.strip("'")
        i += 1
    return args


def validate_args(args: list, n_args: int) -> int:
    """validate the presence or abscence of required
    parameters and prints appropriate error messages"""

    if len(args) == 0:
        print("** class name missing **")
        return -1
    if args[0] not in HBNBCommand._classes:
        print("** class doesn't exist **")
        return -1
    if len(args) < 2 and n_args >= 2:
        print("** instance id missing **")
        return -1
    return 0


def check_params(args: list) -> list:
    valid = []
    for param in args:
        param_type = str
        is_valid = 1
        name, value = None, None
        try:
            name, value = param.split('=')
        except ValueError:
            pass
        if not value:
            continue
        try:
            param_type = HBNBCommand._types[name]
        except KeyError:
            pass
        if param_type == float:
            match = re.search(r'\d+\.\d+', value)
            if not match or (match and match.group() != value):
                continue
        elif param_type == int:
            match = re.search(r'\d+', value)
            if not match or (match and match.group() != value):
                continue
        else:
            if value[0] != '"' or value[-1] != '"':
                is_valid = 0
                continue
            value = value.strip('"').replace('_', ' ')
            quote_idx = [i for i, v in enumerate(value) if v == '"']
            for idx in quote_idx:
                try:
                    if value[idx - 1] != '\\':
                        is_valid = 0
                        break
                except IndexError:
                    is_valid = 0
                    break
        if is_valid:
            valid.append("{}={}".format(name, value.replace('\\', '')))

    return valid


if __name__ == "__main__":
    HBNBCommand().cmdloop()
