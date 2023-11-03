#!/usr/bin/python3
from functools import reduce
print(reduce(lambda x, _: print(chr(x), end=''), range(65, 91), None), end='\n')
