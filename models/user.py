#!/usr/bin/python3

"""
class User inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Public Attributes are email,password,first_name,last_name
    All are Empty strings
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
