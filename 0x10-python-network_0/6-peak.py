#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""
def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    else:
        i = 1
        while i < len(list_of_integers):
            if list_of_integers[i - 1] <= list_of_integers[i] and list_of_integers[i + 1] <= list_of_integers[i]:
                return list_of_integers[i]
            i = i + 1
        return None
