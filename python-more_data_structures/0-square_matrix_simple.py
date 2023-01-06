#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    lst = []
    for i in matrix:
        a = map(lambda i: i*i, i)
        lst.append(list(a))
    return lst
