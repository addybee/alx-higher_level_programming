#!/usr/bin/python3
# prints the result of the addition of all arguments
from sys import argv
sum = 0
for argument in argv[1:]:
    sum += int(argument)
print(sum)
