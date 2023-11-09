#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    else:
        best = 0
        for item in a_dictionary:
            if best < a_dictionary.get(item):
                best = a_dictionary.get(item)
                best_name = item
        return item
