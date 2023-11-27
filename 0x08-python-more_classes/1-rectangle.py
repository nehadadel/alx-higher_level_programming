#!/usr/bin/python3
"""defines a Rectangle"""


class Rectangle:
    """A simple class representing a rectangle.
    
    Attributes:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with given length and width.

        Parameters:
        - length (float): The length of the rectangle.
        - width (float): The width of the rectangle.
        """
        self.width = width
        self.height = height


    def width(self):
        """
        get the width of rectangle
        """
        return (self.__width)


    def width(self, value):
        """
        set the value of width
        
        Attributes:
        - value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        """
        get the hight of rectangle
        """
        return (self.__height)

    def height(self, value):
        """
        set the value of height
        
        Attributes:
        - value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    pass
