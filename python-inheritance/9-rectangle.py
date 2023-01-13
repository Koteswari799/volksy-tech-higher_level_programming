#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry"""


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry
    """

    def _init_(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that calculates area of rectangle
        """

        return self._width * self._height

    def _str_(self):
        """Magic method to return rectangle description
        """

        return "[Rectangle] {}/{}".format(self._width, self._height)
