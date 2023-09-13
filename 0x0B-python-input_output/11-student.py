#!/usr/bin/python3
"""
A class Student that defines a student by
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a Class Student.

        Args:
            first_name (str): The Students first name.
            last_name (str): The students last name.
            age (int): The age of the student.
        """
         self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): A dictionary containing attribute key and values.
        """
         for key, v in json.items():
             setattr(self, key, v)
