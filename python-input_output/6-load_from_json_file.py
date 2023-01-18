#!/usr/bin/python3
'''write a file'''
import json


def load_from_json_file(filename):
    '''file name'''

    with open(filename, mode='r', encoding='UTF-8') as f:
        return json.load(f)
