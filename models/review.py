#!/usr/bin/python3

"""
class Review inherits from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public attributes are place_id, user_id,text
    All are empty strings
    """

    place_id = ""
    user_id = ""
    text = ""
