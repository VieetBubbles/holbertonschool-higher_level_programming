#!/usr/bin/python3
def fizzbuzz():
    print("1", end=" ")
    for number in range(2, 101):
        if number % 3 == 0 and number % 5 == 0:
            print(" FizzBuzz", end="")
        elif number % 3 == 0:
            print(" Fizz", end="")
        elif number % 5 == 0:
            print(" Buzz", end="")
        else:
            print(" {:d}".format(number), end=" ")
