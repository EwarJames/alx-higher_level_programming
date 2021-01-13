#!/usr/bin/python3
"""Defines class Rectangle"""


class Rectangle:
    """Represent class Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle

        Args:
            width (int): Width of the Rectangle
            height (int): Height of the Rectangle

        Return:
              Area and perimeter of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retrieves the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """"Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))
