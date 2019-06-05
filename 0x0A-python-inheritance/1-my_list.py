#!/usr/bin/python3
"""
The 1-my_list module
"""


class MyList(list):
    """A MyList class"""

    def print_sorted(self):
        """method that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
