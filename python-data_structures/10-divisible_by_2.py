#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        lst = []
        for i in my_list:
            if i % 2 == True or i % 2 != False:
                lst.append(i)
        return lst
