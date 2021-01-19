#!/usr/bin/python3
"""Define a class MyList."""


class MyList(list):
    """
    Implements sorted printing for the built-in class - list
    """
    def print_sorted(self):
        """Prints a list in a sorted ascending order."""
        print(sorted(self))
