#!/usr/bin/python3
# checks for lowercase character.
def islower(c):
    if ord(c) in range(ord('a'), ord('z') + 1):  # iterate from a-z
        return True
    return False
