#!/usr/bin/python3
"""
The Matrix division module
"""


def matrix_divided(matrix, div):
    """
    Function that takes a matrix and divides it by div.
    Args:
        matrix: the matrix used for the division.
        div: the number to divided the matrix elements by.
    Return:
          a new matrix with the quotient as elements.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    elif div is 0:
        raise ZeroDivisionError("division by zero")

    if matrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    row_length = 0
    new_list = []

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if row_length == 0:
            row_length = len(row)
            if row_length is 0:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
        else:
            if row_length != len(row):
                raise TypeError("Each row of the matrix must have"
                                " the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            else:
                new_row.append(round(element / div, 2))

        new_list.append(new_row)
    return (new_list)
