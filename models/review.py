#!/usr/bin/python3
"""Review class modules
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class review objects
    """

    place_id = ""
    user_id = ""
    text = ""
