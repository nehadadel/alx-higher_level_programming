#!/usr/bin/python3
letter = 97
while letter <= 122:
    if letter != 113 and letter != 101:
        print("{}".format(chr(letter)), end="")
    letter += 1
