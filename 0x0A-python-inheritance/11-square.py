#!/usr/bin/python3
""" task 9 """


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """Area method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """integer_validator function"""
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')


""" class rectangle """


class Rectangle(BaseGeometry):
    """ Rectangle"""
    def __init__(self, width, height):
        """ init """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ area"""
        return self.__width * self.__height

    def __str__(self):
        """Overcharge __str__"""
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string


""" class squre """


class Square(Rectangle):
    """ squre """
    def __init__(self, size):
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """ area """
        return self.__size ** 2

    def __str__(self):
        """Overcharge __str__"""
        string = "[Square] " + str(self.__width) + "/" + str(self.__height)
        return string
