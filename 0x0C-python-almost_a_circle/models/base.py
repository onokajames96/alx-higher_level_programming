#!/usr/bin/python3
"""Module for Base class"""
import json
import csv


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
