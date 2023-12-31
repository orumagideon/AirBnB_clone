#!/usr/bin/python3
"""
    Module defines the Review class, inheriting from BaseModel
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        Function Initializes Review instance
        """
        super().__init__(*args, **kwargs)
