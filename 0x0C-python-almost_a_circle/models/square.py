#!/usr/bin/python3
"""Defines class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate
            y (int): The y-coordinate
            id (int): The idenity of the new square.
        """
        super().__init__(id, x, y, size, size)

    @property
    def size(self):
        """Set/Get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square

        Args:
            *args (ints): New attribute values.
                1st argument represents id attribute
                2nd argument represents size attribute
                3rd argument represents x attribute
                4th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for w, h in kwargs.items():
                if w == "id":
                    if h is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = h
                elif w == "size":
                    self.size = h
                elif w == "x":
                    self.x = h
                elif w == "y":
                    self.y = h

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
