from calculators.gpa import calculate_gpa


def test_gpa():

    courses = [
        {"grade": "A", "credits": 3},
        {"grade": "B+", "credits": 3},
        {"grade": "B", "credits": 4}
    ]

    result = calculate_gpa(courses)

    assert result > 0
