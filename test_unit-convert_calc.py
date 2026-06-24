from calculators.unit_converter import km_to_miles
from calculators.unit_converter import miles_to_km


def test_km_to_miles():

    assert km_to_miles(10) == 6.21


def test_miles_to_km():

    assert round(miles_to_km(6.21), 0) == 10
