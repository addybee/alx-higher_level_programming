#!/usr/bin/python3
# prints a string in uppercase followed by a new line.
def uppercase(str):
    for i in str:  # iterate through the str
        char = i
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            char = f"{ord(i) - 32:c}"
        print(char, end="")
    print()
