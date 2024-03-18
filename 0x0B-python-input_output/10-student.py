#!/usr/bin/python3


"""student class"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs = None:
            return vars(self)

        new_dictionary = {}
        for key, vlaue in vars(self):
            if key in attrs:
                new_dictionary[key] = value
        return new_dictionary

            
