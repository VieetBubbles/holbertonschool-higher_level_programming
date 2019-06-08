#!/usr/bin/python3
"""
The 14-pascal_triangle.py module.
"""


def pascal_triangle(n):
    """
    function that returns a list of lists of integers representing
    the Pascal’s triangle of n

    Args:
        n - an integer
    Return:
        a list of lists of integers representing
        the Pascal’s triangle of n
    """
    empty = []

    if n <= 0:
        return empty

    pascal_t = []
    row = []

    for number in range(n):
        row = [1]
        if number > 0:
            for j in range(number):

                # formula for pascal triangle
                row.append(sum(pascal_t[-1][j:j + 2]))

        # create list of lists
        pascal_t.append(row)
    return pascal_t
