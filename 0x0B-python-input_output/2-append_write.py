#!/usr/bin/python3
"""define a function to append a string."""


def append_write(filename="", text=""):
    """
    Function that appends a srting at the end of a text.

    Args:
       filename (str): file to be appended.
       text (str): text to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
