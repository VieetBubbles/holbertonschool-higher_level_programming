#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0;

    set_list = set(my_list)

    for _ in set_list:
        sum += _
    return sum
