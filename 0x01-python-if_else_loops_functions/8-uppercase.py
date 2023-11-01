#!/usr/bin/python3
# prints a string in uppercase followed by a new line.
def uppercase(str):
    result = ""
    for i in str:  # iterate through the str
        if ord('a') <= ord(i) <= ord('z'):
            result += f"{ord(i) - 32:c}"
        else:
            result += i
    print(result)
