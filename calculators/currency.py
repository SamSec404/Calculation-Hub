# calculators/currency.py

import json


def load_currencies():

    try:
        with open(
            "data/currencies.json",
            "r"
        ) as file:

            return json.load(file)

    except FileNotFoundError:

        return {}


def convert_currency(
        amount,
        from_currency,
        to_currency
):

    currencies = load_currencies()

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in currencies:
        return "Invalid source currency."

    if to_currency not in currencies:
        return "Invalid target currency."

    # Convert to PKR first
    amount_in_pkr = (
        amount * currencies[from_currency]
    )

    result = (
        amount_in_pkr /
        currencies[to_currency]
    )

    return round(result, 2)
