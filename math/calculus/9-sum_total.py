#!/usr/bin/env python3
"""Summation of squares function"""


def summation_i_squared(n):
    """Calculate sum of squares from 1 to n"""
    if not isinstance(n, int) or n <= 0:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
  
