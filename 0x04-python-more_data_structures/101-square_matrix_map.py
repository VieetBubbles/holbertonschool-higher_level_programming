#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda out: list(map(lambda num: num**2, out)), matrix))
