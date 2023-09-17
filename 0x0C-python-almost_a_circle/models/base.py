#!/usr/bin/python3


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
