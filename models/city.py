#!/usr/bin/python3

"""
Module that creates a User class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel
    """
    state_id = ""
    name = ""
