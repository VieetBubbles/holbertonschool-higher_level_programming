#!/usr/bin/python3
"""
The 0-read_file moduke.
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    Args:
        filename - the name of the file needed to read
    """
    with open(filename, 'r') as f:
        read_var = f.read()
        print(read_var, end="")
