#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        best_name = max(a_dictionary, key=lambda key: a_dictionary[key])
        return best_name
