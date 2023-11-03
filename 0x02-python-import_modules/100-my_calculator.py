#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    ops = ['+', '-', '*', '/']
    if argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[2] == '+':
            func = add
        if argv[2] == '-':
            func = sub
        if argv[2] == '*':
            func = mul
        if argv[2] == '/':
            func = div
        result = func(int(argv[1]), int(argv[3]))
        print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
