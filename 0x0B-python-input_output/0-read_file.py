#!/usr/bin/python3
def read_file(filename=""):
    """ read file """
    with open(filename, 'r', encoding="UTF8") as f:
        read_data = f.read()
        print(read_data)
