#!/usr/bin/python3
'''class'''


class Square:
    '''square size'''
    def __init__(self, size=0):
        '''constructor'''
        if type(size) is not int:
            raised TypeError('size must be an integer')
        if size < 0:
            raised ValueError('size must be >= 0')
        self.__size = size
