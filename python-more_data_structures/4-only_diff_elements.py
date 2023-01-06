#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lst=[]
    for i not in set_1:
        for i not in set_2:
            lst.append(i)
    return lst
