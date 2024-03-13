#!/usr/bin/python3
"""task5"""


import json


def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string"""
    return json.dumps(my_str)
