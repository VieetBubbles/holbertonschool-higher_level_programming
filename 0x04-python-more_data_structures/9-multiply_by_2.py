#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = a_dictionary.copy()

    for x in new_d:
        new_d[x] *= 2

    return new_d
