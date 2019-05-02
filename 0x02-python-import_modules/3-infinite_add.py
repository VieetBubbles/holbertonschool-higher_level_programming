#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    argc = len(argv)
    for _ in range(1, argc):
        sum += int(argv[_])
    print("{}".format(sum))
