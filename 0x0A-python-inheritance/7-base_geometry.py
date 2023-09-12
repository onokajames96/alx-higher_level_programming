#!/usr/bin/python3
#James Onoka


class BaseGeometry:
    def area(self):
        """
        Raises:
            Exception: ["area() is not implemented."]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        """
        # Check if the value is not an integer, raise a TypeError.
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        # Check if the value is less than or equal to 0, raise a ValueError.
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
