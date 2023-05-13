#!/usr/bin/python3
"""
module with the class 'FileStorage' which:
    serializes instances to a JSON file and
    deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel


class FileStorage():
    """ class to handle file storage """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ returns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    def save(self):
        """ serializes __objects to JSON file of path:
                        __file_path
        """
        with open(self.__file_path, "w") as f:
            j_dict = dict()
            for key, val in self.__objects.items():
                j_dict[key] = val.to_dict()
            json.dump(j_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects if file exists
            else: raise no error, do nothing
        """
        try:
            with open(self.__file_path, "r") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))  # create object and store in self.__objects
        except FileNotFoundError:
            return
