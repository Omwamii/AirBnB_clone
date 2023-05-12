#!/usr/bin/python3
"""
module with the class 'FileStorage' which:
    serializes instances to a JSON file and
    deserializes JSON file to instances
"""
import json


class FileStorage():
    """ class to handle file storage """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """ returns the dict __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.__dict__

    def save(self):
        """ serializes __objects to JSON file of path:
                        __file_path
        """
        j_string = json.dumps(self.__objects, default=str)
        with open(self.__file_path, "w") as f:
            f.write(j_string)

    def reload(self):
        """ deserializes the JSON file to __objects if file exists
            else: raise no error, do nothing
        """
        try:
            with open(self.__file_path, "r") as f:
                load_dict = json.load(f)
        except Exception:
            pass
        else:
            for key, val in load_dict.items():
                self.__objects[key] = val
