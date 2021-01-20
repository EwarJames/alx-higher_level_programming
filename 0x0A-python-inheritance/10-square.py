#!/usr/bin/python3
"""Define a Recatngle sub class Square."""
Rectangle = __import__("9-rectangle").Rectangle


def Square(Rectangle):
    """Represent class Square."""

    def __init__(self, size):
        """
        Initialize a new square.

        Args:
            size (int): The size of the square
    """
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size
