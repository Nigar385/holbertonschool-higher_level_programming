#!/usr/bin/env python3
"""Module for calculating polynomial derivatives."""


def poly_derivative(poly):
    """Calculates the derivative of a polynomial.

    Args:
        poly (list): list of coefficients

    Returns:
        list: new list of coefficients of the derivative
        None: if poly is invalid
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 1:
        return [0]

    return [i * poly[i] for i in range(1, len(poly))]
