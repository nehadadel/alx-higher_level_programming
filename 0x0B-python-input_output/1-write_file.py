#!/usr/bin/python3
"""task1"""


def write_file(filename="", text=""):
    """writes a string to a file, returns the number of characters written"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
