#!/usr/bin/python3
"""
Super class that all other objects inherit from.
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    __init__ method -> should handles input from other methods from BaseModel
    __str__ method -> should returns class name, id, and a dictionary
    """

    def __str__(self):
        """
        Returns the class name, id, and the dictionary to be printed
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

        def __init__(self, *args, **kwargs):
            """
            Initiating the BaseModel class to be able to accept arguments\
         Converting self.created_at and self.updated_at into datetime objects
            if the incoming argument is a dictionary
            If they aren't a dictionary, call a function that turns them into
            a dictionary.
            """

        formating = "%Y-%m-%d %H:%M:%S.%f"
        change = 0
        for arg in args:
            if type(arg) is dict:
                change = 1
                self.created_at = datetime.strptime(arg["created_at"], formating)
                self.updated_at = datetime.strptime(arg["updated_at"], formating)
                self.__dict__ = args
            if change == 0:
                self.created_at = datetime.now()
                self.id = str(uuid4())
                from models.__init__ import storage

                storage.new(self)
