#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = list(map(lambda search: search.replace(search, replace), my_list))
    return my_list
