#!/usr/bin/python3


"""json"""


import json


def load_from_json_file(filename):
    """ load from json file"""
    with open(filename, "r") as read_file:
        return json.load(read_file)
