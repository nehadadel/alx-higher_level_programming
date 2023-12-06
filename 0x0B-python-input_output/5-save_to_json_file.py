#!/usr/bin/python3


"""json"""


import json


def save_to_json_file(my_obj, filename):
    """ save to json file """
    with open(filename, "w") as write_file:
        json.dump(my_obj, write_file)
