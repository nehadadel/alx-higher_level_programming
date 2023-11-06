#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    else:
        res = list(bytearray(len(my_list)))
        i = 0;
        while i < len(my_list):
            if my_list[i] % 2 == 0:
                res[i] = True
            else:
                res[i] = False
            i += 1
        return res
