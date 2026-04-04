#!/usr/bin/python3
"""This module defines a square with size validation using property."""


class Square:
    """Defines a square with a private size attribute and area method."""

    def __init__(self, size=0):
        """Initialize a square with optional size."""
        self.size = size  # setter is used here

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size
