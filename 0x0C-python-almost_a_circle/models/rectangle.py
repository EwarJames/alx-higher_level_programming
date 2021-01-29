#!/usr/bin/python3
"""Define class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represent Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): x-coordinate of the Rectangle.
            y (int): y-coordinate of the Rectangle.

        Raises:
           TypeError: If either width or height is not int.
           TypeError: If either x or y is not an integer.
           ValueError: If either width or height <= 0.
           ValueError: If either x or y is less than 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Set/Gets the width of the Rectangle."""
        self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Set/Gets the height of the Rectangle."""
        self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Set/Gets the x-coordinate of the Rectangle."""
        self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Set/Gets the y-coordinate of the Rectangle."""
        self.__y

    @y.setter
    def y(self, value):
        self.__y = value
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Retrun the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with character '#'
        """
        if self.width = 0 or self.height = 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle.

        Args:
            1st argument represents the id attribute
            2nd argument represents the width attribute
            3rd argument represents the height attribute
            4th argument represents the x attribute
            5th argument represents the y attribut.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.x)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for w, h in kwargs.items():
                if w == "id":
                    if h is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = h
                elif w == "width":
                    self.width = h
                elif w == "height":
                    self.height = h
                elif w == "x":
                    self.x = h
                elif w == "y":
                    self.y = h

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns Rectangle overriding overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)
