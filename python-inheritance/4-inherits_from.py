#!/usr/bin/python3
"""This module defines a function that checks inheritance."""


def inherits_from(obj, a_class):
    """
    Return True if obj is a subclass instance of a_class.
    Otherwise return False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
