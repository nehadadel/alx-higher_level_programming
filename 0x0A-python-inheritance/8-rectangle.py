#!/usr/bin/python3
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
        self.width = width
        self.height = height
