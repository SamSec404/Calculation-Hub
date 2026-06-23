from calculators.scientific import square_root
from calculators.scientific import factorial
from calculators.scientific import logarithm
from calculators.scientific import power


def test_square_root():

    assert square_root(25) == 5


def test_factorial():

    assert factorial(5) == 120


def test_logarithm():

    assert logarithm(100) == 2


def test_power():

    assert power(2, 3) == 8