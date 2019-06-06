#!/usr/bin/python3
"""
The 4-append_write module.
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename - the name of the file that needs to be written into.
        text - the text thatis to be placed into the file.
    """
    with open(filename, 'a') as f:
        characters = f.write(text)

    return characters
