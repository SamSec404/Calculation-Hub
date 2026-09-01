from calculators.bmi import calculate_bm

def test_bmi():
    bmi = calculate_bmi(70, 1.75)
    assert bmi > 20



