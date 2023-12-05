#!/usr/bin/python3
"""hello """


def append_write(filename="", text=""):
    """append"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
