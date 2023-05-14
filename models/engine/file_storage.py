#!/usr/bin/python3
"""
<<<<<<< HEAD
Contains the FileStorage class model


"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
=======
module with the class 'FileStorage' which:
    serializes instances to a JSON file and
    deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
>>>>>>> 572b624ea5abdcb37e998e9157d8dd835ed89b80
from models.place import Place
from models.review import Review


<<<<<<< HEAD
class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the `obj` with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serialize __objects to the JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        -> Only IF it exists!
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
=======
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
>>>>>>> 572b624ea5abdcb37e998e9157d8dd835ed89b80
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
