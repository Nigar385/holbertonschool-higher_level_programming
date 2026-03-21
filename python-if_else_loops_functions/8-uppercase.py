#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase without using str.upper()."""
    for c in str:
        #  ^yg ^yr ki  ik h ^yrfdirs ^y, b  y  k h ^yrf ^y   evir
        if ord('a') <= ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
