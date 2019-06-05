#!/usr/bin/python3
"""
The 0-lookup module
"""


def lookup(obj):
    """
    function that returns the list of available attributes and
    methods of an object.
    Args:
        obj - the object to lookup
    Return:
        a list object.
    """
    return dir(obj)
