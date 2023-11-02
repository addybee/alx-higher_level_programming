#!/usr/bin/python3
# import argv from sys
if __name__ == "__main__":
    import sys
    argv = sys.argv
    length = len(argv) - 1
    if length == 0:
        print(f"{length} arguments.")
    else:
        if length == 1:
            print(f"{length:d} argument:\n1: {argv[length]}")
        else:
            print(f"{length:d} argument:")
            for i, item in enumerate(argv[1:]):
                i += 1
                print(f"{i}: {item}")
