#!/usr/bin/env python3
"""the program that serves as the entry point to the command
line interpreter for the Airbnb console"""
import cmd
import readline
import re
import sys
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
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
    }


    def do_EOF(self, arg):
        """Exits the interpreter. USAGE: EOF\n"""
        sys.exit(0)

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        sys.exit(0)

    def do_create(self, arg):
        """creates a new instance of a class passed as argument.\
 USAGE: create <class_name>"""
        if arg == "":
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = HBNBCommand.__classes[arg]()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

    def do_show(self, arg):
        args = parse_args(arg)
        print(args)
        for item in args:
            print(item)

    def emptyline(self):
        return

def parse_args(arg: str) -> list:
    regex = re.compile(r'("*\w+\s*\w+"*)')
    arg_list = regex.findall(arg)
    i = 0
    while i < len(arg):
        curr_arg = ""
        j = i + 1
        while arg[j] not in ('"', " "):
            i += 1

    """i = 0
    while i < len(arg):
        idx = i + 1
        if arg[i] == '"':
            print(arg[i])
            while idx < len(arg):
                if arg[idx] == '"':
                    break
                idx += 1
            print(f"i: {i}, idx: {idx}")
            if arg[idx] == '"':
                arg_list.append(arg[i:idx + 1])
        if idx - 1 != i:
            i = idx
        i += 1"""
    return arg_list


if __name__ == "__main__":
    HBNBCommand().cmdloop()
