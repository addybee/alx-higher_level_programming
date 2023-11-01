#!/usr/bin/python3
# checks for lowercase character.
def islower(c):
    for ch in range(ord('a'), ord('z') + 1):  # iterate from a-z
        if ch == c:
            return True
    return False
