#!/usr/bin/python3


"""
class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.integer_validator("width", width, False)
        self.integer_validator("height", height, False)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        self.integer_validator("width", width, False)
        self.__width = width

    @height.setter
    def height(self, height):
        self.integer_validator("height", height, False)
        self.__height = height

    @x.setter
    def x(self, x):
        self.integer_validator("x", x)
        self.__x = x

    @y.setter
    def y(self, y):
        self.integer_validator("y", y)
        self.__y = y

    def integer_validator(self, name, value, flag=True):
        """integer_validator function"""
        if type(value) != int:
            raise TypeError(name + ' must be an integer')
        if value <= 0 and flag is False:
            raise ValueError(name + ' must be > 0')
        elif value < 0 and flag is True:
            raise ValueError(name + ' must be >= 0')

    def area(self):
        "area of rectanglar"
        return self.__width * self.__height

    def display(self):
        "that prints in stdout the Rectangle instance with the character #"
        for b in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * ' ', end='')
            print(self.__width * '#')

    def __str__(self):
        "__str__"
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

    def update(self, *args):
        " that assigns an argument to each attribute:"
        self.id = args[0]
        self.width = args[1]
        self.height = args[2]
        self.x = args[3]
        self.y = args[4]
