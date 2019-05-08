#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []

    for _ in my_list:
        if _ % 2 == 0:
            return new_list.append(True)
        else:
            return new_list.append(False)
    return new_list
