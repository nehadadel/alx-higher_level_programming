#!/usr/bin/python3
#!/usr/bin/python3
"""Square Class

defining the square

"""


class Square:
    """a 2d square"""
    try:
        def __init__(self, size=0):
            self.__size = size
    except TypeError:
        print("size must be an integer")
        

    pass
