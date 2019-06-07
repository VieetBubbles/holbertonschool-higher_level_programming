#!/usr/bin/python3
"""
The 12-student module.
"""


class Student:
    """The class Student"""
    def __init__(self, first_name, last_name, age):
        """initialize the object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that retrieves a dictionary representation of a Student instance
        Args:
            attrs - a list of strings or not
        """
        if type(attrs) is list and all(type(st) is str for st in attrs):
            dictionary = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    dictionary[key] = value
            return dictionary
        else:
            return self.__dict__
