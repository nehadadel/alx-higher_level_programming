#!/usr/bin/python3
""" task 1 """


def write_file(filename="", text=""):
    """writ"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
