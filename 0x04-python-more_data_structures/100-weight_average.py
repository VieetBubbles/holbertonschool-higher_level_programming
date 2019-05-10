#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    return sum(_[0] * _[1] for _ in my_list) / sum(n[1] for n in my_list)
