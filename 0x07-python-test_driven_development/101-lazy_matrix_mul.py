#!/usr/bin/python3
"""
The lazy multiplication module using numpy
"""


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Return:
          The a matrix with product of the two matrix's elements
    """
    import numpy as np

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not len(m_a):
        raise ValueError("m_a can't be empty")

    if not len(m_b):
        raise ValueError("m_b can't be empty")

    if any(not len(row) for row in m_a):
        raise ValueError("m_a can't be empty")

    if any(not len(row) for row in m_b):
        raise ValueError("m_b can't be empty")

    new_matrix = []

    new_matrix = np.dot(m_a, m_b)

    return new_matrix
