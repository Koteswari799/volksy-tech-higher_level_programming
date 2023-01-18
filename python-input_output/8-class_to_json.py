#!/usr/bin/python3
'''write a file'''
import json


def class_to_json(obj):
    '''create a file'''
    return obj.__dict__
