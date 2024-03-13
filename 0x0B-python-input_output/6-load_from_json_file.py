#!/usr/bin/python3
"""task6"""


import json


def load_from_json_file(my_obj, filename):
    """ that creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
