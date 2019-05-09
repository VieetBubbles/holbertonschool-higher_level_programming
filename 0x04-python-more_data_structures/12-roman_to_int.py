#!/usr/bin/python3
def roman_to_int(roman_string):
    my_dict = {'M': 1000, 'D': 500, 'C': 100,
               'L': 50, 'X': 10, 'V': 5, 'I': 1}

    sum = 0
    prev_rn = 0

    if not isinstance(roman_string, str):
        return 0

    if roman_string is None:
        return 0

    for _ in roman_string:
        if _ in my_dict:
            # Handles highest to lowest order
            if my_dict[_] <= prev_rn:
                sum += my_dict[_]
                prev_rn = my_dict[_]
            # Handles lowest to highest order and single r_numerals
            else:
                sum += my_dict[_] - prev_rn * 2
                prev_rn = my_dict[_]
    return sum
