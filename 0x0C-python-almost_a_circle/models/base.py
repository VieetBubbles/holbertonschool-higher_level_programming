#!/usr/bin/python3
"""
The base module.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method that returns the JSON string representation
        of list_dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes the JSON string representation
        of list_objs to a file.
        """
        file_name = cls.__name__ + ".json"
        new_ob_list = []

        if list_objs is not None:
            for _ in list_objs:
                new_ob_list.append(cls.to_dictionary(_))

        with open(file_name, 'w') as f:
            f.write(cls.to_json_string(new_ob_list))
