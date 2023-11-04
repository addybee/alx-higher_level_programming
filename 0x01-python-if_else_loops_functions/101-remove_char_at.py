#!/usr/bin/python3
#  creates a copy of the string, removing the character at the position n
def remove_char_at(str, n):
    if n < 0:
        return str
    cpy_str = str[:n] + str[n + 1:]
    return cpy_str
