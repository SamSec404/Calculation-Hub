# calculators/age.py

from datetime import date


def calculate_age(birth_year):

    current_year = date.today().year

    return current_year - birth_year


def age_in_months(age):

    return age * 12


def age_in_days(age):

    return age * 365
