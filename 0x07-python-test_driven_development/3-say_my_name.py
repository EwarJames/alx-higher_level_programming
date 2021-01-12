#!/usr/bin/python3
"""Define a function that prints my names."""


def say_my_name(first_name, last_name=""):
    """
    Prints names.

    Args:
        first_name: First name to be printed.
        last_name: Last name to be printed.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
