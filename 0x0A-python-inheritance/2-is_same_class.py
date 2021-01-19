#!/usr/bin/python3
"""Defines a function that checks for two classes"""


def is_same_class(obj, a_class):
    """
    Chscks if an objectt is exactly an instance of a specified class.

    Args:
        obj : The object to check.
        a_class : class to compare to.

    Return:
        True: if the object is exactly an instance of class
        False: Otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
