#!/usr/bin/env python3

def poly_derivative(poly):
    # Yoxlama
    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    # Sabit funksiyanın törəməsi
    if len(poly) == 1:
        return [0]

    # Törəmə hesabla
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])

    return derivative
