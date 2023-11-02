#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{} arguments".format(len(argv) - 1), end="")
    if len(argv) - 1 == 0:
        print(".")
    else:
        print(":")
        i = 1
        while i <= len(argv) - 1:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
