#!/usr/bin/python3
"""
module with 'Review' class
"""
from .base_model import BaseModel


class Review(BaseModel):
    """ 'Review' class """
    place_id = ""
    user_id = ""
    text = ""
