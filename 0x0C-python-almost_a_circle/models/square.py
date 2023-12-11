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

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.integer_validator("width", value, False)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        "that assigns attributes:"
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        "that returns the dictionary representation of a square:"
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
