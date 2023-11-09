#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    output = 0
    roman_string = roman_string.upper()
    roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                 "M": 1000}
    roman_keys = list(roman_dic)
    for idx, val in enumerate(roman_string):
        if idx < (len(roman_string) - 1):
            if roman_keys.index(val) < roman_keys.index(roman_string[idx+1]):
                output -= roman_dic[val]
                continue
        output += roman_dic[val]
    return output
