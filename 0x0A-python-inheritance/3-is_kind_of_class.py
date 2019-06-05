#!/usr/bin/python3
"""
The 3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of, or if the
    object is an instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj - the object
        a_class - the type or class that object should be
    Return:
        True if object's type is the same as a_class, or false if not
    """
    return isinstance(obj, a_class)
