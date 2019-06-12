#!/usr/bin/python3
"""
The base module.
"""


class Base:
    """
    The Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize the base class.
        Args:
            id - assume it is an integer.
        """
        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id
