#!/usr/bin/python3
"""
The 1-number_of_lines module.
"""


def number_of_lines(filename=""):
    """
    function that returns the number of lines of a text file
    Args:
        filename - the name of the file that needs to be read
    """
    count = 0

    with open(filename, 'r') as f:
        for line in f:
            count += 1

    return count
