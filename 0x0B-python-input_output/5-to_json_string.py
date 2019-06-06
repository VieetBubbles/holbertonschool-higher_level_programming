#!/usr/bin/python3
"""
The 5-to_json_string module.
"""


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)

    Args:
        my_obj - the object (string)
    """
    from json import dumps
    return dumps(my_obj)
