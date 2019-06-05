#!/usr/bin/python3
"""
The 4-inherits_from module.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj - the object
        a_class - the type or class that object should be
    Return:
        True if object's type is the same as a_class, or false if not
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
