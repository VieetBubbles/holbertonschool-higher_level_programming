g#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    argc = len(argv)

    operator = {'+': add, '-': sub, '*': mul, '/': div}

    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] in operator:
        num1 = int(argv[1])
        num2 = int(argv[3])
        math = operator[argv[2]]
        result = math(num1, num2)
        print("{} {} {} = {}".format(num1, argv[2], num2, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
