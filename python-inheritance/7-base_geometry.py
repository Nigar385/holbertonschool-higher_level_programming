#!/usr/bin/python3
"""
create empty class
"""


class BaseGeometry:
    """empty class"""

    def area(self):
        """if area is not defined, raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate that value is a positive integer"""
        if (type(value) is not int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
