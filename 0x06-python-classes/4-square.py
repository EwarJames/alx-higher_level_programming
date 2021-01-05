#!/usr/bin/python3
"""Defines a class square."""


class Square:
    """Class square with private attribute instance"""
    def __init__(self, size=0):
        """Ïnitialize a new Square with size argument"""
        self.size = size

    def area(self):
        """"Return the current Square area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
