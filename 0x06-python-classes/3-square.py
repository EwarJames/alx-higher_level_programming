#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Class square with private attribute instance"""
    def __init__(self, size=0):
        """Ïnitialize a new Square with size argument"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """"Return the current Square area"""
        return (self.__size * self.__size)
