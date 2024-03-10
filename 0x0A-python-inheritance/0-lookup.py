#!/usr/bin/python3
"""hello"""


def lookup(obj):
    """returns the list of available attributes and methods of an object:"""
    return (list(dir(obj)))
