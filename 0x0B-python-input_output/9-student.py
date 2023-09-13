#!/usr/bin/python3
"""
A class Student that defines a student by:

Public instance attributes
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The Students last name.
            age (int): Students age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student
        instance (same as 8-class_to_json.py)
        """
        return self.__dict__
