#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc > 2:
        print("{} arguments:".format(argc - 1))
    else:
        print("1 argument:")
    for _ in range(1, argc):
        print("{}: {}".format(_, argv[_]))
