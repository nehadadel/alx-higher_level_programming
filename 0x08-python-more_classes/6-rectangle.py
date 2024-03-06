#!/usr/bin/python3
"""defines a Rectangle"""


class Rectangle:
    '''A simple class representing a rectangle. '''
    number_of_instances = 0

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
        number_of_instances += 1
        self.value_validation(width, "width")
        self.__width = width
        self.value_validation(height, "height")
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        size = "#" * self.__width
        rect = []
        for index in range(self.__height):
            rect.append(size)
        return "\n".join(rect)

    def __repr__(self):
        return "{}({}, {})".format((type(self).__name__),
                                   self.__width, self.__height)

    def __del__(self):
        number_of_instances -= 1
        print('Bye rectangle...')
