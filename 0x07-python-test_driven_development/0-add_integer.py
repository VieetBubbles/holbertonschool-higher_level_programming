#!/usr/bin/python3
"""
The adding 2 integers Module
"""
def add_integer(a, b=98):
    """
    Python function that adds 2 integers
    Args:
        a: the 1st integer
        b: the 2nd integer

    Return:
          the sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
