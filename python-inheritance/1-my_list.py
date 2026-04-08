#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""


class MyList(list):
    """MyList is a subclass of list that prints a sorted version of itself."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
