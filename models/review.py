#!/usr/bin/python3
<<<<<<< HEAD
"""Contains the Review model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Implements the Review model"""
=======
"""
module with 'Review' class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """ 'Review' class """
>>>>>>> 572b624ea5abdcb37e998e9157d8dd835ed89b80
    place_id = ""
    user_id = ""
    text = ""
