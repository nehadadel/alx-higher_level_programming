#!/usr/bin/python3
"""finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):

    if not list_of_integers or list_of_integers is None:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    if list_of_integers[0] > list_of_integers [1]:
        return list_of_integers[0]

    if list_of_integers[-1] > list_of_integers [-2]:
        return list_of_integers[-1]

    if len(list_of_integers) == 3:
        if (list_of_integers[1] >= list_of_integers[0]
            and list_of_integers[1] >= list_of_integers[2]):
            return list_of_integers[1]
    
    mid = int(len(list_of_integers) / 2)
    i = 1
    while i < len(list_of_integers) - mid - 1:
        if (list_of_integers[i - 1] <= list_of_integers[i]
                and list_of_integers[i + 1] <= list_of_integers[i]):
                return list_of_integers[i]
        i = i + 1
    i = mid + 1
    while i < len(list_of_integers) - 1:
        if (list_of_integers[i - 1] <= list_of_integers[i]
                and list_of_integers[i + 1] <= list_of_integers[i]):
                return list_of_integers[i]
        i = i + 1
    return None

