#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    for item in new_dic:
        new_dic[item] = 2 * new_dic[item]
    return new_dic
