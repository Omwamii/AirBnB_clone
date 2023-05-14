#!/usr/bin/python3
"""
    BnB interpreter programm
"""
import cmd
import json
import sys
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
        """Quit command to exit the program\n """
        sys.exit()

    def do_EOF(self, line):
        """ handle EOF """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel or User, saves it
            and prints the id
        - if class name missing (one arg) print: ** class name missing **
        - if class name doesn't exist print ** class doesn't exist **
        """
        ln = line.split()
        if len(ln) == 0:
            print("** class name  missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(ln[0])().id)  # create obj using eval and print id
            storage.save()

    def do_show(self, line):
        """
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
            print("** instance id is missing **")
        else:
            try:
                with open("file.json", "r") as f:
                    obj_dicts = json.load(f)
                    if f"{ln[0]}.{ln[1]}" not in obj_dicts:
                        print("** no instance found **")
                    else:
                        obj_dict = obj_dicts[f"{ln[0]}.{ln[1]}"]
                        print(f"[{ln[0]}] ({obj_dict['id']}) {obj_dict}")
            except FileNotFoundError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
            Deletes an instance based on class name and id & saves
            changes to the json file
            - if cls-name missing: print ** class name missing **
            - if cls doesnt exist: print ** class doesn't exist **
            - if id is missing: print ** instance id missing **
            - if instance for the id !exist: print ** no instance found **
        """
        ln = line.split()
        if len(ln) == 0:
            print("** class is missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(ln) == 1:
            print("** instance id is missing **")
        else:
            try:
                with open("file.json", "r") as f:
                    obj_dicts = json.load(f)
            except FileNotFoundError:
                print("** no instance found **")
            else:
                if f"{ln[0]}.{ln[1]}" not in obj_dicts:
                    print("** no instance found **")
                else:
                    obj_dicts.pop(f"{ln[0]}.{ln[1]}")  # delete obj from dict
                with open("file.json", "w") as f:
                    j_string = json.dumps(obj_dicts)
                    f.write(j_string)  # write updated dict JSON string
                storage.reload()

    def do_all(self, line):
        """
            prints all string rep of all instances based or not on cls-name
                $ all (ok)   $ all <class name> (ok)
        """
        ln = line.split()
        if len(ln) > 0 and ln[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            objs = list()
            try:
                with open("file.json", "r") as f:
                    obj_dicts = json.load(f)
            except FileNotFoundError:
                pass
            else:
                for key, val in obj_dicts.items():
                    n = key.split(".")
                    if len(ln) == 0:
                        objs.append(f"[{n[0]}] ({n[1]}) {val}")
                    else:
                        if n[0] == ln[0]:
                            objs.append(f"[{n[0]}] ({n[1]}) {val}")
            print(objs)

    def do_update(self, line):
        """
            Use: update <class name> <id> <attribute name> <"attribute value">

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
        ln = line.split()
        if len(ln) == 0:
            print("** class name missing **")
        elif ln[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(ln) == 1:
            print("** instance id missing **")
        elif len(ln) == 2:
            print("** attribute name missing **")
        elif len(ln) == 3:
            print("** value missing **")
        else:
            try:
                with open("file.json", "r") as f:
                    obj_dicts = json.load(f)
            except FileNotFoundError:
                print("** no instance found **")
            else:
                if f"{ln[0]}.{ln[1]}" not in obj_dicts:
                    print("** no instance found **")
                else:
                    value = (cast_type)(ln[3][1:-1])  # remove double quotes ""
                    if f"{ln[0]}.{ln[1]}" in obj_dicts:
                        obj_dict = obj_dicts[f"{ln[0]}.{ln[1]}"]
                        cast_type = type(obj_dict[f"{ln[2]}"])
                        val = cast_type(value)
                        obj_dict[ln[2]] = val  # update the val in the obj dict
                        obj_dicts[f"{ln[0]}.{ln[1]}"] = obj_dict
            with open("file.json", "w") as f:
                j_string = json.dumps(obj_dicts)
                f.write(j_string)  # write the new dict to file


if __name__ == '__main__':
    HBNBCommand().cmdloop()
