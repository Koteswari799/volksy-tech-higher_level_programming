#!/usr/bin/python3
'''string'''


def write_file(filename="", text=""):
    '''file name'''
    with open(filename, mode='w', encoding='UTF-8') as f:
        return (f.write(text))
