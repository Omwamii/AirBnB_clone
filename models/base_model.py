#!/usr/bin/python3
"""
<<<<<<< HEAD
A module that implements the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    A class that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the string representation of BaseModel object.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        return dict_1
=======
module with the Base class
"""
import datetime
import uuid
import models


class BaseModel():
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        """ init vars """
        if kwargs:
            for key, value in kwargs.items():
                val = value
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    form = "%Y-%m-%dT%H:%M:%S.%f"
                    val = datetime.datetime.strptime(value, form)
                setattr(self, key, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at  # new instance no changes
            models.storage.new(self)

    def __str__(self):
        """ define __str__ """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with current datetime when the object is changed
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dict containing all keys/values
        of __dict__ of the instance.
            - Only instance attributes set are returned (self.__dict__)
            - __class__ key must be added to the dict with name of class
            - created_at and updated_at must be converted to string obj
                in ISO format
        """
        my_dict = dict()
        for key, val in self.__dict__.items():
            my_dict[key] = val
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()

        return my_dict
>>>>>>> 572b624ea5abdcb37e998e9157d8dd835ed89b80
