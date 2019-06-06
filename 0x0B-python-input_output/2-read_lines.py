#!/usr/bin/python3
"""
The 2-read_lines module.
"""


def read_lines(filename="", nb_lines=0):
    """
    function that reads n lines of a text file (UTF8) and prints it to stdout
    Args:
        filename - the name of the file that needs to be read
        nb_lines - the number of lines
    """
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            var_read = f.read()
            print(var_read, end="")

        else:
            for line in f:
                if (nb_lines is not 0):
                    print(line, end="")
                    nb_lines -= 1
