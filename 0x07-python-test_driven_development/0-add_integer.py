#!/usr/bin/python3
"""Defining a function"""


def add_integer(a, b=98):
    """Function that adds two integers.
       Args:
             a - first integer to be added
             b  - second integer to be added
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
