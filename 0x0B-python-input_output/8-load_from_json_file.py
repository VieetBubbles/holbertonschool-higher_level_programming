#!/usr/bin/python3
"""
The 8-load_from_json_file module.
"""


def load_from_json_file(filename):
    """
    function that creates an Object from a “JSON file”.
    Args:
        filename - the file to use to create an object
    """
    from json import loads
    with open(filename, 'r') as f:
        return loads(f.read())
