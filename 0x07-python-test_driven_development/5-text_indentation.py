#!/usr/bin/python3
"""
The text indentation module
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after each of these
    characters: ., ? and :
    Args:
        text: the string that is to be broken down
    """
    new_sentence = ""
    after_ns_space = True

    if type(text) != str:
        raise TypeError("text must be a string")

    for c in text.strip():

        if c is " " and after_ns_space is True:
            pass

        elif c in ".?:":
            new_sentence += c + "\n\n"
            after_ns_space = True

        else:
            new_sentence += c
            after_ns_space = False

    print(new_sentence, end="")
