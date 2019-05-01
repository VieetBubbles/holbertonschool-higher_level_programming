#!/usr/bin/python3
def uppercase(str):
    for character in str:

        uc = ord(character)

        if uc >= 97 and uc <= 122:
            uc_word = chr(uc - 32)
        else:
            uc_word = character
        print("{:s}".format(uc_word), end="")

    print()
