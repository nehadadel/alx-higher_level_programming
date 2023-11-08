#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_dic = sorted(list(a_dictionary))
    for item in list_dic:
        print(item, end=": ")
        print(a_dictionary.get(item))
