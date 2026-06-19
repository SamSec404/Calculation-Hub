from Calculators.basic_calc import add
from Calculators.basic_calc import subtract
from Calculators.basic_calc import multiply
from Calculators.basic_calc import divide
from Calculators.basic_calc import modulus
from Calculators.basic_calc import power


def test_add():

    assert add([10, 20, 30]) == 60


def test_subtract():

    assert subtract([100, 20, 10]) == 70


def test_multiply():

    assert multiply([2, 3, 4]) == 24


def test_divide():

    assert divide([100, 2, 5]) == 10


def test_modulus():

    assert modulus(10, 3) == 1


def test_power():

    assert power(2, 3) == 8