#!/usr/bin/python3
"""Defines class Base."""
import json
import csv
import turtle


class Base:
    """Represent class Base."""

    __nb_objects = 0

    def __init__(self, id="None"):
        """
        Initializes new class Base.

        Args:
            id (int)=reference to the id of the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list-dictionaries (list): List of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write JSON serialization of a list of file's objects.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") jsnfile:
            if list_objs is None:
                jsnfile.write("[]")
            else:
                list_dicts = [(i.to_dictionary() for i in list_objs)]
                jsnfile.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of the JSON string representation.

        Args:
            json_string (str): A JSON string representation of list of dicts.
        """
        if json_string is None or json string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instantiated with all attributes already set.

        Args:
           **dictionary (dict): key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                i = cls(1, 1)
            else:
                i = cls(1)
            new.update(**dictionary)
            return i

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.

        Return:
            If the file does not exist, empty list.
            Otherwise, list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsnfile:
                list_dicts = Base.from_json_string(jsnfile.read())
                return [cls.create(**dict) for dict in list_dicts]
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Write the csv serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "height", "width", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                w = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for ob in list_objs:
                    w.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a csv file.

        Returns:
            If the file does not exist, an empty list.
            Otherwise, a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, filenames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dict.items())
                              for dict in list_dicts]
                return [cls.create(**diict) for dict in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangle, list_square):
        """
        Draw Rectangles and Squares using the turtle module.
        
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
