#!/usr/bin/python3
"""
add task0
alx
by : nehadadel
"""


def add_integer(a, b=98):
    """
    add_integer function
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
