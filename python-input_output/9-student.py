#!/usr/bin/python3
'''write a file'''


class Student:
    '''create a class'''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''create a function'''

        return self.__dict__
