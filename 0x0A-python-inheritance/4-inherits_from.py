#!/usr/bin/python3
""" task 3"""


def inherits_from(obj, a_class):
    """ inherits """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
