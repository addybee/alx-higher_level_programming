#!/usr/bin/python3
for dig in range(89):
    if dig % 10 > dig / 10:
        print("{:02d}".format(dig), end=", ")
print("{:02d}".format(dig + 1))
