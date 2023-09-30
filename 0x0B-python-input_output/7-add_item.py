#!/usr/bin/python3
"""
Adds all arguments to a Python list
and saves them to a JSON file.
"""
import sys
import json
import os.path

json_filename = 'add_item.json'

if os.path.exists(json_filename):
    with open(json_filename, 'r') as file:
        obj_json_file = json.load(file)

else:
    obj_json_file = []

obj_json_file.extend(sys.argv[1:])
with open(json_filename, 'w') as file:
    json.dump(obj_json_file, file)
