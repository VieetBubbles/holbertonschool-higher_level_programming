#!/usr/bin/python3
"""
The 2-is_same_class module.
"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False.
    Args:
        obj - the object.
        a_class - the type of class.
    Return: true if the object is the same type as a_class or false if not.
    """
    return (type(obj) is a_class)
