#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{} argument".format(len(argv) - 1), end="")
    if len(argv) - 1 == 0:
        print("s.")
    elif len(argv) - 1 == 1:
        print(":")
        print("1: {:s}".format(argv[1]))
    else:
        print("s:")
        i = 1
        while i <= len(argv) - 1:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1
