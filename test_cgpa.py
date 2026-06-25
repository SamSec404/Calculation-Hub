from calculators.cgpa import calculate_cgpa


def test_cgpa():

    gpas = [3.5, 3.7, 3.8]

    assert calculate_cgpa(gpas) == 3.67
