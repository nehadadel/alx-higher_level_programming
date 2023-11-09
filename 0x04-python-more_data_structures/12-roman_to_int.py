#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        count = 0
        r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        r_num2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        for key in r_num2:
            if key in roman_string:
                count += r_num2.get(key)
                roman_string = roman_string.replace(key, "")
        for ch in roman_string:
            for key in r_n:
                if ch == key:
                    count += r_n.get(key)
                    break
        return count
