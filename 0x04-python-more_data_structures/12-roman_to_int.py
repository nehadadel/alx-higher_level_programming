#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        count = 0
        roman_number = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        roman_number2 = {'IV' : 4, 'IX' : 9, 'XL' : 40, 'XC' : 90, 'CD' : 400, 'CM' : 900}
        for key in roman_number2:
            if key in roman_string:
                count += roman_number2.get(key)
                roman_string = roman_string.replace(key, "")
        for ch in roman_string:
            for key in roman_number:
                if ch == key:
                    count += roman_number.get(key)
                    break
        return count
