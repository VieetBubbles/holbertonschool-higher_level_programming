#!/usr/bin/python3
"""
The 10-class_to_json module.
"""


def class_to_json(obj):
    """
    function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object.

    Args:
        obj - the object used to return it's dictionary description.
    """
    return obj.__dict__
