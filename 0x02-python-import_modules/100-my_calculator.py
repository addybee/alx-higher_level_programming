#!/usr/bin/python3
# imports all functions from the file calculator_1.py and handles basic
# operations.
from calculator_1 import add, sub, mul, div
from sys import argv
if len(argv)!= 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit (1)
operators = ["+", "-", "*", "/"]
if argv[2] not in operators:
    print("Unknown operator. Available operators: +, -, * and /")
    exit (1)
if argv[2] == operators[0]:
    print(f"{argv[1]} + {argv[3]} = {add(int(argv[1]), int(argv[3]))}")
elif argv[2] == operators[1]:
    print(f"{argv[1]} - {argv[3]} = {sub(int(argv[1]), int(argv[3]))}")
elif argv[2] == operators[2]:
    print(f"{argv[1]} * {argv[3]} = {mul(int(argv[1]), int(argv[3]))}")
elif argv[2] == operator[3]:
    print(f"{argv[1]} / {argv[3]} = {div(int(argv[1]), int(argv[3]))}")


