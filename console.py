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

        match = re.search(r'(\w+)\.(\w+)\((.*?)\)', line)
        if match:
            class_name = match.group(1)
            method = match.group(2)
            arguments = match.group(3)
            arguments = arguments.split(", ")
            arguments = [arg.strip('"') for arg in arguments]
            args = class_name + ' ' + ' '.join(arguments)
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
            - if instance of cls-name !exist for id : ** no instance found **
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
                print(objs[f"{ln[0]}.{ln[1]}"].__str__())  # print __str__

    def do_count(self, line):
        """ count occurences """
        pass

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
        Usage: update <class name> <id> <attribute name> <"attribute value">

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
        if len(ln) == 0:
            print("** class name missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(ln) == 1:
            print("** instance id missing **")
        elif len(ln) > 1 and len(ln) < 4:
            if f"{ln[0]}.{ln[1]}" not in objs:
                print("** no instance found **")
                return
            if len(ln) == 2:
                print("** attribute name missing **")
            if len(ln) == 3:
                print("** value missing **")
        else:
            value = ln[3][1:-1]  # remove the ""
            if f"{ln[0]}.{ln[1]}" not in objs:
                print("** no instance found **")
            else:
                obj = objs[f"{ln[0]}.{ln[1]}"]
                if ln[2] in obj.__class__.__dict__.keys():  # attr present
                    cast_type = type(obj.__class__.__dict__[ln[2]])
                    obj.__dict__[ln[2]] = cast_type(value)
                else:  # no need to check type
                    obj.__dict__[ln[2]] = value
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
