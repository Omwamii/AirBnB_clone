#!/usr/bin/python3
"""
    BnB interpreter programm
"""
import cmd
import json
import sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """ Commandline class """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program\n """
        sys.exit()


    def do_EOF(self, line):
        """ handle EOF """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it
            and prints the id 
        - if class name missing (one arg) print: ** class name missing **
        - if class name doesn't exist print ** class doesn't exist **
        """
        l = line.split()
        if len(l) == 0:
            print("** class name  missing **")
        elif l[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            print(new.id)

    def do_show(self, line):
        """
            prints the string rep of an instance based on cls-name & id
            - if cls-name missing: print ** class name missing **
            - if cls-name doesnt exist: print ** class doesn't exist **
            - if id is missing: print ** instance id is missing **
            - if instance of cls-name doesnt exist for id : ** no instance found **
        """
        l = line.split()
        if len(l) == 0:
            print("** class name missing **")
        elif l[0] != "BaseModel":
            print("** class doesn't exist **")
        elif l[1] is None:
            print("** instance id is missing **")
        else:
            with open("file.json", "r") as f:
                obj_dicts = json.load(f)
            if f"{l[0]}.{l[1]}" not in obj_dicts:
                print("** no instance found **")
            else:
                print(f"{l[0]}.{l[1]}.__str__")

    def do_destroy(self, line):
        """
            Deletes an instance based on class name and id & saves 
            changes to the json file
            - if cls-name missing: print ** class name missing **
            - if cls doesnt exist: print ** class doesn't exist **
            - if id is missing: print ** instance id missing **
            - if instance for the id doesn't exist: print ** no instance found **
        """
        l = line.split()
        if len(l) == 0:
            print("** class is missing **")
        elif l[0] != "BaseModel":
            print("** class doesn't exist **")
        elif l[1] is None:
            print("** instance id is missing **")
        else:
            with open("file.json", "rw") as f:
                obj_dicts = json.load(f)
                if f"{l[0]}.{l[1]}" not in obj_dicts:
                    print("** no instance found **")
                else:
                    del obj_dicts[f"{l[0]}.{l[1]}"]  # delete the object from the dict
                    json.dump(obj_dicts, f)  # write the new dict to file

    def do_all(self, line):
        """
            prints all string rep of all instances based or not on cls-name
                $ all (ok)   $ all BaseModel (ok)
        """
        l = line.split()
        try:
            if l[0] != "BaseModel":
                print("** class doesn't exist **")
                return
        except IndexError:
            pass
        all_objs = list()
        with open("file.json", "r") as f:
            obj_dict = json.load(f)
            for obj_id in obj_dict.keys():
                n = obj_id.split(".")
                all_objs.append(f"[{n[0]}] ({n[1]}) {obj_dict[obj_id]}")
            print(all_objs)

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
        l = line.split()
        if len(l) == 0:
            print("** class name missing **")
        elif l[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(l) == 1:
            print("** instance id missing **")
        elif len(l) == 2:
            print("** attribute name missing **")
        elif len(l) == 3:
            print("** value missing **")
        else:
            with open("file.json", "r+") as f:
                obj_dicts = json.load(f)
                if f"{l[0]}.{l[1]}" not in obj_dicts:
                    print("** no instance found **")
                else:
                    updated_dict = obj_dicts[f"{l[0]}.{l[1]}"]
                    updated_dict[l[2]] = l[3]  # update the value in the obj dict
                    obj_dicts[f"{l[0]}.{l[1]}"] = updated_dict
                    json.dump(obj_dicts, f)  # write the new dict to file


if __name__ == '__main__':
    HBNBCommand().cmdloop()
