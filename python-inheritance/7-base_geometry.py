#!/usr/bin/python3
"""This module defines a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raise an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
