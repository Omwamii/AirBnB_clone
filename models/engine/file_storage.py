#!/usr/bin/python3
"""
module with FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
                    # create object and store in self.__objects
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
