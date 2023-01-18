#!/usr/bin/python3
'''string'''


def read_file(filename=""):
    '''file name'''
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
