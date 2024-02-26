#!/usr/bin/python3
"""Square Class

defining the square

"""


class Square:
    """a 2d square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if any(not (isinstance(v, int))
               and v < 0 for v in position) and len(position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if all(not (isinstance(v, int))
               and v < 0 for v in value) and len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                print(" " * self.__position[0], end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
