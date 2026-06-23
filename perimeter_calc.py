# calculators/perimeter.py

import math


def rectangle_perimeter(length, width):

    return 2 * (length + width)


def square_perimeter(side):

    return 4 * side


def circle_circumference(radius):

    return round(2 * math.pi * radius, 2)


def triangle_perimeter(side1, side2, side3):

    return side1 + side2 + side3
