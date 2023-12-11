#!/usr/bin/python3


"""
class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @size.setter
    def size(self, size):
        self.integer_validator("size", size, False)
        self.__width = size
        self.__height = size

    @property
    def size(self):
        '''Size of this square.'''
        return self.width
