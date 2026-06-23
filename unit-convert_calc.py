# calculators/unit_converter.py

def km_to_miles(km):

    return round(km * 0.621371, 2)


def miles_to_km(miles):

    return round(miles / 0.621371, 2)


def celsius_to_fahrenheit(celsius):

    return round((celsius * 9/5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit):

    return round((fahrenheit - 32) * 5/9, 2)


def kg_to_pounds(kg):

    return round(kg * 2.20462, 2)


def pounds_to_kg(pounds):

    return round(pounds / 2.20462, 2)
