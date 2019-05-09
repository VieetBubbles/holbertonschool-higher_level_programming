#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for _, m in enumerate(my_list):
        new_list.append(replace if m == search else m)

    return (new_list)
