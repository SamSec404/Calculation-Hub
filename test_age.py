from calculators.age import age_in_months
from calculators.age import age_in_days


def test_age_months():

    assert age_in_months(20) == 240


def test_age_days():

    assert age_in_days(1) == 365
