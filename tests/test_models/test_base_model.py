#!/usr/bin/python3

"""
unit test for ./models/base_model.py
Run with: python -m unittest test_module
"""


from models.base_model import BaseModel
import unittest
import uuid


class TestBaseModel(unittest.TestCase):

    """Template Test Case for the BaseModel class.
    Function:
            something()
    """

    def testing_base(self):
        """
        Generic testing_base function
        """
        self.testUp()


if __name__ == "__main__":
    unittest.main()
