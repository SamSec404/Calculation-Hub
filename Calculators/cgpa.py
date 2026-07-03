# calculators/cgpa.py

def calculate_cgpa(gpas):

    if len(gpas) == 0:
        return 0

    return round(sum(gpas) / len(gpas), 2)
