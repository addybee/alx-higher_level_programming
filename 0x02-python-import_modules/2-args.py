#!/usr/bin/python3
# import argv from sys
if __name__ == "__main__":
    from sys import argv
    length = len(argv[1:])
    print("{:d} {:s}{:s}".format(length, "arguments" if length != 1 else
        "argument", ":" if length != 0 else "."))
    if length > 0:
        for index, item in enumerate(argv[1:]):
            index += 1
            print(f"{index}: {item}")
