#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    length = range(len(str))
    for i in length:
        if i != n:
            copy += str[i]
    return (copy)
