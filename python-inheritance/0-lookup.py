#!/usr/bin/python3
"""
This module defines a function that returns the list of attributes
and methods available for a given object.
"""


def lookup(obj):
    """
    Return a list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods will be listed.

    Returns:
        A list containing the names of the attributes and methods of obj.
    """
    return dir(obj)
