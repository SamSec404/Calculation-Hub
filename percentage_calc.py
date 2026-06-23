# calculators/percentage.py

def calculate_percentage(obtained_marks, total_marks):

    if total_marks == 0:
        return "Error: Total marks cannot be zero"

    return round((obtained_marks / total_marks) * 100, 2)


def percentage_increase(old_value, new_value):

    if old_value == 0:
        return "Error: Old value cannot be zero"

    increase = ((new_value - old_value) / old_value) * 100

    return round(increase, 2)


def percentage_decrease(old_value, new_value):

    if old_value == 0:
        return "Error: Old value cannot be zero"

    decrease = ((old_value - new_value) / old_value) * 100

    return round(decrease, 2)
