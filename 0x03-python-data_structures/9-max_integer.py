#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None

    maximum = my_list[0]

    for _ in my_list[1:]:
        if maximum < _:
            maximum = _
    return maximum
