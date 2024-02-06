#!/usr/bin/python3
""" defines a function that adds all arguments to a Python list, and then save
    them to a file
"""


import os
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

file_data = []
arguments = argv[1:]

if os.path.exists("./add_item.json") and os.path.isfile("./add_item.json"):
    file_data = load_from_json_file("add_item.json")

for i in arguments:
    file_data.append(i)

save_to_json_file(file_data, "add_item.json")
