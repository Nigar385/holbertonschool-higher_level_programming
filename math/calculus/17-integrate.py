#!/usr/bin/env python3
"""Module for polynomial integration."""


def poly_integral(poly, C=0):
    """Calculates the integral of a polynomial.

    Args:
        poly (list): list of coefficients
        C (int): constant of integration

    Returns:
        list: integral polynomial or None if invalid
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not isinstance(C, int):
        return None

    result = [C]

    for i, coef in enumerate(poly):
        if not isinstance(coef, (int, float)):
            return None

        value = coef / (i + 1)

        # integer check
        if value == int(value):
            value = int(value)

        result.append(value)

    # remove trailing zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result
