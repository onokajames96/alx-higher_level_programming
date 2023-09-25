#!/usr/bin/python3
"""Module for Base class"""
import json
import csv
import turtle


class Base:
    """
    Base class for managing id attributes of other classes.

    Attributes:
        __nb_objects (int): A private class attribute to keep track of the
            number of objects created from the Base class.
        id (int): A public instance attribute representing the unique ID of
            an instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        A new instance of the Base class Initialized.

        Args:
            id (int, optional): The ID to assign to the instance. If not
                provided, a new ID will be generated automatically.

        Returns:
            None
        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serialize a list of dictionaries to a JSON string.

        Returns the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string([obj.to_dictionary()
                                         for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Converts a JSON string to a list of dictionaries."""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of the class with attributes set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns A list of instances."""
        filename = cls.__name__ + ".json"
        instances = []

        try:
            with open(filename, "r") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                instances = [cls.create(**item) for item in list_dicts]
        except FileNotFoundError:
            pass

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and write in CSV."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                else:
                    fieldnames = []

                if fieldnames:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    for obj in list_objs:
                        writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a CSV file and creates objects."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                obj_list = csv.DictReader(csvfile, fieldnames=fieldnames)
                obj_list = [dict([key, int(val)] for key, val in m.items())
                            for m in obj_list]
                return [cls.create(**m) for m in obj_list]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw a list of rectangles and squares using the Turtle module."""
        screen = turtle.Screen()
        screen.bgcolor("DarkRed")

        t = turtle.Turtle()
        t.pensize(3)
        t.shape("turtle")

        def draw_shape(shape, color):
            """Draw a list of shapes with a specified color."""
            t.color(color)
            for item in shape:
                t.showturtle()
                t.penup()
                t.goto(item.x, item.y)
                t.down()
                for _ in range(2):
                    t.forward(item.width)
                    t.left(90)
                    t.forward(item.height)
                    t.left(90)
                t.hideturtle()

            draw_shape(list_rectangles, "White")
            draw_shape(list_squares, "LightBlue")

            turtle.exitonclick()
