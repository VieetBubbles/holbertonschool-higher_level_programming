#!/usr/bin/python3
"""
The 7-save_to_json_file module
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation.
    Args:
        my_obj - the object
        filename - the file that needs to be written to
    """
    from json import dumps
    with open(filename, 'w') as f:
        f.write(dumps(my_obj))
