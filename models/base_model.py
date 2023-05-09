#!/usr/bin/python3
"""
module with the Base class
"""
import datetime
import uuid


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
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ define __str__ """
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dict containing all keys/values
        of __dict__ of the instance.
            - Only instance attributes set are returned (self.__dict__)
            - __class__ key must be added to the dict with name of class
            - created_at and updated_at must be converted to string obj
                in ISO format
        """
        self.save()
        my_dict = dict()
        for key, val in self.__dict__.items():
            if not key.startswith('__') and not callable(val):
                my_dict[key] = val
        my_dict['__class__'] = __class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()

        return my_dict
