from calculators.currency import convert_currency


def test_currency():

    result = convert_currency(
        100,
        "USD",
        "PKR"
    )

    assert result == 28000
