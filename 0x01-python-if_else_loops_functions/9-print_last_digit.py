#!/usr/bin/python3
def print_last_digit(number):

    if number < 0:
        # can also be written as abs(number) % 10
        number *= -1
    last_digit = number % 10

    print("{:d}".format(last_digit), end="")

    return(last_digit)
