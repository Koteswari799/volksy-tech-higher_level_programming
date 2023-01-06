#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = [:]
    for i in my_list:
        if lst[i] == search:
            lst[i] = replace
    return lst

