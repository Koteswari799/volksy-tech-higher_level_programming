#!/usr/bin/python3
'''write a file'''
import json


def save_to_json_file(my_obj, filename):
    '''file name'''
    with open(filename, mode='w', encoding='UTF-8') as f:
        return(f.write(json.dumps(my_obj)))
