#!/usr/bin/env python3
"""the program that serves as the entry point to the command
line interpreter for the Airbnb console"""
import cmd
import readline
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
    _classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Place": Place,
            "Amenity": Amenity,
            "Review": Review,
    }

    def do_EOF(self, arg: str) -> None:
        """Exits the interpreter. USAGE: EOF\n"""
        sys.exit(0)

    def do_quit(self, arg: str) -> None:
        """Quit command to exit the program\n"""
        sys.exit(0)

    def emptyline(self):
        return

    def default(self, arg: str) -> None:
        args = parse_args(arg, delim=".")
        if len(args) < 2:
            super().default(arg)
            return
        class_name = args[0]
        command = args[1]
        if command == "all()":
            self.onecmd(f"{command.replace('()', '')} {class_name}")
        elif command == "count()":
            count = self.do_all(f"{class_name}", count=True)
            print(count)

    def do_create(self, arg: str) -> None:
        """creates a new instance of a class passed as argument.\
 USAGE: create <class_name>"""
        args = parse_args(arg)
        if validate_args(args, 1) == -1:
            return
        if args[0] in HBNBCommand._classes:
            new_obj = HBNBCommand._classes[args[0]]()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)

    def do_show(self, arg: str) -> None:
        """prints the str representation of an instance.\
 USAGE: show <classname> <id>"""
        args = parse_args(arg)
        if validate_args(args, 2) == -1:
            return
        key = f"{args[0]}.{args[1]}"
        all_obj = storage.all()
        if key in all_obj:
            obj_class = HBNBCommand._classes[args[0]]
            obj = obj_class(**all_obj[key])
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg: str) -> None:
        """deletes a given instance from storage.\
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
        """prints all instances. USAGE: all <classname> or all"""
        args = parse_args(arg)
        obj_list = []
        if len(args) > 0:
            if validate_args(args, 1) == -1:
                return
            obj_class = HBNBCommand._classes[args[0]]
            for key, obj_dict in storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj_class(**obj_dict)))
            if count:
                return len(obj_list)
            print(obj_list)
            return
        for key, obj_dict in storage.all().items():
            class_name = obj_dict["__class__"]
            obj_class = HBNBCommand._classes[class_name]
            obj_list.append(str(obj_class(**obj_dict)))
        print(obj_list)

    def do_update(self, arg: str) -> None:
        """update the given attribute of a given object.\
 USAGE: update <class name> <id> <attr name> '<attr value>'"""
        args = parse_args(arg)
        if validate_args(args, 4) == -1:
            return
        key = f"{args[0]}.{args[1]}"
        all_obj = storage.all()
        if key not in all_obj:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr = args[2]
        value = args[3]
        obj_dict = all_obj[key]
        obj = BaseModel(**obj_dict)
        if attr in obj.__dict__:
            attr_type = type(obj.__dict__[attr])
            obj.__dict__[attr] = attr_type(value)
        else:
            obj.__dict__[attr] = value
        all_obj[key] = obj.to_dict()
        storage.save()


def parse_args(arg: str, delim=" ") -> list:
    if arg == "":
        return []
    args = arg.split(delim)
    i = 0
    while i < len(args):
        curr = args[i]
        found = 0
        if curr[0] == '"':
            if i == len(args) - 1:
                args[i] = curr.replace('"', '')
                break
            for j in range(i + 1, len(args)):
                next = args[j]
                if next[len(next) - 1] == '"':
                    found = 1
                    break
            full = curr
            for k in range(i + 1, j + 1):
                full += f" {args[k]}"
            full = full.replace('"', '')
            args.insert(i, full)
            args_copy = args.copy()
            for k in range(i + 1, j + 2):
                args.pop(args.index(args_copy[k]))
        i += 1
    return args


def validate_args(args: list, n_args: int) -> int:
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
