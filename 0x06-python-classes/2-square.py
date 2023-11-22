#!/usr/bin/python3
#!/usr/bin/python3
"""Square Class

defining the square

"""


class Square:
    """a 2d square"""
    def __init__(self, size=0):
        if not type(x) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    pass
