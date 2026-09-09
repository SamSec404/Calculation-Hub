# calculators/gpa.py

GRADE_POINTS = {
    "A": 4.00,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.00,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.00,
    "C-": 1.67,
    "D+": 1.33,
    "D": 1.00,
    "F": 0.00
}


def calculate_gpa(courses):

    total_points = 0
    total_credits = 0

    for course in courses:

        grade = course["grade"].upper()
        credits = course["credits"]

        if grade not in GRADE_POINTS:
            continue

        total_points += GRADE_POINTS[grade] * credits
        total_credits += credits

    if total_credits == 0:
        return 0

    return round(total_points / total_credits, 2)
