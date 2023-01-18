#!/usr/bin/python3
'''write a file'''


def append_write(filename="", text=""):
    '''append'''
    with open(filename, mode='a', encoding='UTF-8') as f:
        return (f.write(text))
