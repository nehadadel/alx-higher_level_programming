#!/usr/bin/python3
""" task0 """


def read_file(filename=""):
    """ read file """
    with open(filename, "r", encoding="UTF-8") as f:
        read_data = f.read()
        print(read_data, end="")
