#!/usr/bin/python3
s = range(65, 91)
print reduce(lambda x, y: str(x) +str(y), s)
