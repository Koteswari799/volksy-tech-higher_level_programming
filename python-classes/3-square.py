#!/usr/bin/python3
'''square'''


class Square:
    '''square size'''
    def __init__(self, size=0):
        '''constuctor'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Area of square'''
        return (self.__size * self.__size)
