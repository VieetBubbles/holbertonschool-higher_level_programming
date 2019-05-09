#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        for x in a_dictionary:
            if x == key:
                a_dictionary[x] = value
                sorted(a_dictionary)
                return a_dictionary

    if key not in a_dictionary:
        a_dictionary[key] = value
        sorted(a_dictionary)
        return a_dictionary
