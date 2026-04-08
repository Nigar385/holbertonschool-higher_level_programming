#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """Raise exception for area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate integer value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

