#!/usr/bin/python3
"""
The print my name is - module
"""
def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>.
    Args:
        first_name: a string of the person's first name
        last_name: a string of the person's last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
