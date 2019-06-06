#!/usr/bin/python3
"""
The 3-write_file module.
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename - the name of the file that needs to be written into
        text - the text thatis to be placed into the file
    """
    with open(filename, 'w') as f:
        return f.write(text)
