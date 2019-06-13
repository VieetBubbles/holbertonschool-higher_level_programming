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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []

        return json.dumps(list_dictionaries)

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

    @staticmethod
    def from_json_string(json_string):
        """
        static method  that returns the list of
        the JSON string trepresentation json_string.
        """
        if json_string is None or len(json_string) is 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes already set.
        """
        if cls.__name__ is "Rectangle":
            dummy_ob = cls(4, 3)

        if cls.__name__ is "Square":
            dummy_ob = cls(8)

        dummy_ob.update(**dictionary)

        return dummy_ob

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances.
        """
        file_name = cls.__name__ + ".json"
        new_ob_list = []

        with open(file_name, 'r') as f:
            new_ob_list = cls.from_json_string(f.read())

        for index, value in enumerate(new_ob_list):
            new_ob_list[index] = cls.create(**new_ob_list[index])

        return new_ob_list
