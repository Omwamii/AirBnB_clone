#!/usr/bin/python3
"""
    BnB interpreter programm
"""
import cmd
import json
import re  # regex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Commandline class """
    prompt = '(hbnb) '
    __classes = ["BaseModel",
                 "User",
                 "State",
                 "City",
                 "Amenity",
                 "Place",
                 "Review"
                 ]

    def do_quit(self, line):
        """Quit command to exit the program.

        """
        return True

    def do_EOF(self, line):
        """ EOF signal to exit the program. """
        return True

    def emptyline(self):
        pass

    def default(self, line):
        """ define default for uknown syntax """
        cmds = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update
                }

        match = re.search(r'(\w*)\.(\w+)\((.*?)\)', line)  # rgx to find match
        # () in rgx to grp items e.g \w+ to refer to later using match.group()
        if match:
            class_name = match.group(1)
            method = match.group(2)
            arguments = match.group(3)
            dict_arg = ""  # harmless incase dict not found
            if "{" in arguments and "}" in arguments:  # find if dict in args
                dict_index = arguments.index("{")
                dict_arg = arguments[dict_index:]  # prevent split ","
                arguments = arguments[:dict_index]
            arguments = arguments.split(", ")
            arguments = [arg.strip('"') for arg in arguments]
            args = class_name + ' ' + ' '.join(arguments) + ' ' + dict_arg
            if method in cmds:
                return cmds[method](args)  # call method
        print(f"*** Unknown syntax: {line}")
        return False

    def do_create(self, line):
        """ Creates a new instance of a class, saves it
            and prints the id
        - if class name missing (one arg) print: ** class name missing **
        - if class name doesn't exist print ** class doesn't exist **
        """
        ln = line.split()
        if len(ln) == 0:
            print("** class name missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(ln[0])().id)  # create obj using eval and print id
            storage.save()

    def do_show(self, line):
        """
            Usage: show <class> <id>
            prints the string rep of an instance based on cls-name & id
            - if cls-name missing: print ** class name missing **
            - if cls-name doesnt exist: print ** class doesn't exist **
            - if id is missing: print ** instance id is missing **
            - if instance of cls !exist for id : ** no instance found **
        """
        ln = line.split()
        if len(ln) == 0:
            print("** class name missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(ln) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            if f"{ln[0]}.{ln[1]}" not in objs:
                print("** no instance found **")
            else:
                print(objs[f"{ln[0]}.{ln[1]}"].__str__())  # print str rep

    def do_count(self, line):
        """
        Usage: <class name>.count()
        retrieve the number of instances of a class
        """
        name = line.strip()
        if name not in self.__classes:
            print(0)
            return
        else:
            objs = list()
            count = 0
            objs_dict = storage.all()
            for obj, val in objs_dict.items():
                if name == val.__class__.__name__:
                    count += 1
            print(count)

    def do_destroy(self, line):
        """
        Usage: destroy <class> <id>
        Deletes an instance based on class name and id & saves
        changes to json file
            - if cls-name missing: print ** class name missing **
            - if cls doesnt exist: print ** class doesn't exist **
            - if id is missing: print ** instance id missing **
            - if instance for the id !exist: print ** no instance found **
        """
        ln = line.split()
        if len(ln) == 0:
            print("** class name missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(ln) == 1:
            print("** instance id missing **")
        else:
            objs = storage.all()
            if f"{ln[0]}.{ln[1]}" not in objs:
                print("** no instance found **")
            else:
                objs.pop(f"{ln[0]}.{ln[1]}")  # delete obj from __objects
                storage.save()

    def do_all(self, line):
        """prints all string rep of all instances based or not on cls-name
                $ all (ok)   $ all <class name> (ok)"""
        ln = line.split()
        if len(ln) > 0 and ln[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objs = list()
            objs_dict = storage.all()
            for obj, val in objs_dict.items():
                if len(ln) > 0 and ln[0] == val.__class__.__name__:
                    objs.append(val.__str__())
                elif len(ln) == 0:
                    objs.append(val.__str__())
            print(objs)

    def do_update(self, line):
        """
        Usage: update <class name> <id> <attribute name> <"attr value">
        or <class name>.update(<id>, <attribute name>, <attribute value>)
        or <class name>.update(<id>, <dictionary representation>)
        Updates an instance based on the class name and id by
        adding or updating attribute & save the change to the json file
         - if cls-name missing: print ** class name missing **
         - if cls-name doesn't exist: print ** class doesn't exist **
         - if id is missing: print ** instance id missing **
         - if instance for id doesn't exist: print ** no instance found **
         - if attribute name is missing: print ** attribute name missing **
         - if value for attribute doesn't exist: print ** value missing **
         - The rest of the values should not be used (one attr at a time)
        """
        objs = storage.all()
        ln = line.split()
        try:
            dict_index = line.index("{")
        except ValueError:
            arg = ""
            pass
        else:
            arg = str(line[dict_index:])
        if len(ln) == 0:
            print("** class name missing **")
            return False
        if ln[0] not in self.__classes:
            print("** class doesn't exist **")
            return False
        if len(ln) == 1:
            print("** instance id missing **")
            return False
        if f"{ln[0]}.{ln[1]}" not in objs:
            print("** no instance found **")
            return False
        if len(ln) == 2:
            print("** attribute name missing **")
            return False
        if len(ln) == 3:
            print("** value missing **")
            return False
        if arg.startswith("{") and arg.endswith("}") \
                and isinstance(eval(arg), dict):
            obj = objs[f"{ln[0]}.{ln[1]}"]
            for key, val in eval(arg).items():
                key = key.strip('"')
                if key in obj.__class__.__dict__ and \
                        type(obj.__class__.__dict__[key]) \
                        in {str, float, int}:
                    cast_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = cast_type(val)
                else:
                    obj.__dict__[key] = val
        else:
            value = ln[3].strip('"\'')  # remove the ""
            obj = objs[f"{ln[0]}.{ln[1]}"]
            if ln[2] in obj.__class__.__dict__.keys():  # attr present
                cast_type = type(obj.__class__.__dict__[ln[2]])
                obj.__dict__[ln[2]] = cast_type(value)
            else:  # no need to check type
                obj.__dict__[ln[2]] = value
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
