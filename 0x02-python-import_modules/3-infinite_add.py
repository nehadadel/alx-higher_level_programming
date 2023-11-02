#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0")
    else:
        i = 1
        sum = 0
        while i <= len(argv) - 1:
            sum += int(argv[i])
            i += 1
        print("{}".format(sum))
