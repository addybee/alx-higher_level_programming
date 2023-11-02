#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv[1:]) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = ["+", "-", "*", "/"]
    if argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    answer = 0
    if argv[2] == operators[0]:
        answer = add(int(argv[1]), int(argv[3]))
        print(f"{argv[1]} + {argv[3]} = {answer}")
    elif argv[2] == operators[1]:
        answer = sub(int(argv[1]), int(argv[3]))
        print(f"{argv[1]} - {argv[3]} = {answer}")
    elif argv[2] == operators[2]:
        answer = mul(int(argv[1]), int(argv[3]))
        print(f"{argv[1]} * {argv[3]} = {answer}")
    elif argv[2] == operators[3]:
        answer = div(int(argv[1]), int(argv[3]))
        print(f"{argv[1]} / {argv[3]} = {answer}")
