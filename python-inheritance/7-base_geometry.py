#!/usr/bin/python3
"""
This module defines the BaseGeometry class.
It provides methods for geometric calculations and input validation.
"""


class BaseGeometry:
    """
    A class used to represent base geometry shapes.
    """

    def area(self):
        """
        Public instance method that raises an Exception.
        The area calculation is not yet implemented in this base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
