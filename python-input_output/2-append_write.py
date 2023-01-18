#!/usr/bin/python3
'''string'''


def append_write(filename="", text=""):
    '''file name'''
    if filename:
        with open(filename, mode='a', encoding='UTF-8') as f:
            return (f.write(text)):
