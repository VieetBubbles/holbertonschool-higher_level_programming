#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:

        row_length = len(row)

        for element in range(0, row_length):

            if element < row_length - 1:
                print("{:d}".format(row[element]), end=" ")

            else:
                print("{:d}".format(row[element]))
