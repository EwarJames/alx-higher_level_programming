#!/usr/bin/python3
"""Define a function that writes to a textfile."""


def write_file(filename="", text=""):
    """
    Writes a string to a textfile encoded in utf-8.

    Args:
        filename (str): The name of the file.
        text (str): text to write

    Return:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
