from calculators.percentage import calculate_percentage
from calculators.percentage import percentage_increase
from calculators.percentage import percentage_decrease


def test_percentage():

    assert calculate_percentage(450, 500) == 90.0


def test_percentage_increase():

    assert percentage_increase(100, 120) == 20.0


def test_percentage_decrease():

    assert percentage_decrease(100, 80) == 20.0