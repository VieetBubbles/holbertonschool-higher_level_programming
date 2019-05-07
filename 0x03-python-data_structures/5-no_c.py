#!/usr/bin/python3
def no_c(my_string):

    new_string = ""

    for _ in my_string:
        if (_ != 'c' and _ != 'C'):
            new_string += _
    return new_string
