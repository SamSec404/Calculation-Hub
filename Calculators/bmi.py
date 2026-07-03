# calculators/bmi.py

def calculate_bmi(weight, height):

    if height <= 0:
        return "Error: Height must be greater than zero"

    bmi = weight / (height ** 2)

    return round(bmi, 2)


def bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    return "Obese"
