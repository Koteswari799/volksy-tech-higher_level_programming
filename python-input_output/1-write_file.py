#!/usr/bin/python3
'''string'''


def write_file(filename="", text=""):
    '''file name'''
    with open(filename, 'r',encoding='UTF-8') as f:
        return len(list(f))
