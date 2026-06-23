# calculators/scientific.py

import math


def square_root(number):

    if number < 0:
        return "Error: Cannot calculate square root of negative number"

    return math.sqrt(number)


def factorial(number):

    if number < 0:
        return "Error: Factorial not defined for negative numbers"

    return math.factorial(number)


def logarithm(number):

    if number <= 0:
        return "Error: Logarithm only defined for positive numbers"

    return math.log10(number)


def sine(angle):

    return math.sin(math.radians(angle))


def cosine(angle):

    return math.cos(math.radians(angle))


def tangent(angle):

    return math.tan(math.radians(angle))


def power(base, exponent):

    return math.pow(base, exponent)
