#!/usr/bin/python3
'''list'''


def inherits_from(obj, a_class):
    '''size of list'''

    if type(obj) is a_class or not isinstance(obj, a_class):
        return True
    else:
        return False
