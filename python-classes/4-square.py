#!/usr/bin/python3
"""class"""


class Square:
    """Access and update private attribute"""

    def _init_(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """constructor"""

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of square"""

        return (self._size * self._size)
