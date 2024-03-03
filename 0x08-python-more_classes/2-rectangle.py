#!/usr/bin/python3
"""defines a Rectangle"""


class Rectangle:
    '''A simple class representing a rectangle. '''
    @staticmethod
    def value_validation(value, name):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value < 0:
            raise ValueError(name + " must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.value_validation(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.value_validation(value, "height")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.value_validation(width, "width")
        self.__width = width
        self.value_validation(height, "height")
        self.__height = height

    def area(self):
        return self.__heigth * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__heigth + self.__width)
