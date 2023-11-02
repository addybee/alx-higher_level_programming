#!/usr/bin/python3
# prints all the names defined by the compiled module hidden_4.pyc
import hidden_4
lst = dir(hidden_4)
for item in lst:
    if item[:2] == "__":
        continue
    print(item)
