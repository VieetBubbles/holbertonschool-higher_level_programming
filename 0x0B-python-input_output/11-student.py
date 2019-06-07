#!/usr/bin/python3
"""
The 11-student module.
"""


class Student:
    """The class Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        method that retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
