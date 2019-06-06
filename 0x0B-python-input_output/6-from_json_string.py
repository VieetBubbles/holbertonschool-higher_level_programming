#!/usr/bin/python3
"""
The 6-from_json_string module.
"""


def from_json_string(my_str):
    """
    function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str - the object (Python data structure)
    """
    from json import loads
    return loads(my_str)
