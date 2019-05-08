#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    # tuple_a = (1, 89, 0, 0)
    # tuple_b = (88, 11, 0, 0)

    # tuple_b = (1, 0, 0)
    # tuple_b = (0, 0)

    new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new
