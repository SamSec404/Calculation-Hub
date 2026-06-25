from calculators.area import rectangle_area
from calculators.area import square_area


def test_rectangle_area():

    assert rectangle_area(5, 4) == 20


def test_square_area():

    assert square_area(5) == 25
