#!/usr/bin/python3
"""
The print squares module
"""
def print_square(size):
    """
    Function that prints a square with the character #.
    Args:
        size: the size of the square
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n") * size, end="")
