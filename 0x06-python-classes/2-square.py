#!/usr/bin/python3
"""Defines a class square based on 0-square.py"""


class Square:
    """Class square with private attribute instance, size"""
    def __init__(self, size=0):
        """Ïnitialize a new Square with size argument"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
