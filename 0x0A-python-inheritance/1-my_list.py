#!/usr/bin/python3
"""hello"""


class MyList(list):
    """class MYlist"""
    def print_sorted(self):
        """print sorted list"""
        tmp = self.copy()
        print(sorted(tmp))
