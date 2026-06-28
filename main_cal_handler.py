# ================= IMPORTS =================

from calculators.basic import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    power
)

from calculators.scientific import (
    square_root,
    factorial,
    logarithm,
    sine,
    cosine,
    tangent
)

from calculators.gpa import calculate_gpa
from calculators.cgpa import calculate_cgpa

from calculators.percentage import (
    calculate_percentage,
    percentage_increase,
    percentage_decrease
)

from calculators.bmi import (
    calculate_bmi,
    bmi_category
)

from calculators.age import (
    calculate_age,
    age_in_months,
    age_in_days
)

from calculators.area import (
    rectangle_area,
    square_area,
    circle_area,
    triangle_area
)

from calculators.perimeter import (
    rectangle_perimeter,
    square_perimeter,
    circle_circumference,
    triangle_perimeter
)

from calculators.unit_converter import (
    km_to_miles,
    miles_to_km,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kg_to_pounds,
    pounds_to_kg
)

from calculators.currency import convert_currency

from utils.history import (
    add_history,
    show_history,
    clear_history
)

from utils.validator import (
    get_number,
    get_positive_integer
)

from database.db import create_database


# ================= FUNCTIONS =================

def get_numbers():
    count = get_positive_integer(
        "\nHow many numbers do you want to enter? "
    )

    numbers = []

    for i in range(count):
        number = get_number(
            f"Enter Number {i + 1}: "
        )

        numbers.append(number)

    return numbers


# Create database
create_database()


# ================= MAIN LOOP =================

while True:

    print("\n==============================")
    print("      CALCULATION HUB")
    print("==============================")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Logarithm")
    print("10. GPA Calculator")
    print("11. CGPA Calculator")
    print("12. Percentage Calculator")
    print("13. BMI Calculator")
    print("14. Age Calculator")
    print("15. Area Calculator")
    print("16. Perimeter Calculator")
    print("17. Unit Converter")
    print("18. Currency Converter")
    print("19. Show History")
    print("20. Clear History")
    print("21. Exit")

    choice = input("\nEnter Choice: ")

    # Addition
    if choice == "1":
        numbers = get_numbers()
        result = add(numbers)
        print("Result:", result)
        add_history(f"Addition {numbers} = {result}")

    # Subtraction
    elif choice == "2":
        numbers = get_numbers()
        result = subtract(numbers)
        print("Result:", result)
        add_history(f"Subtraction {numbers} = {result}")

    # Multiplication
    elif choice == "3":
        numbers = get_numbers()
        result = multiply(numbers)
        print("Result:", result)
        add_history(f"Multiplication {numbers} = {result}")

    # Division
    elif choice == "4":
        numbers = get_numbers()
        result = divide(numbers)
        print("Result:", result)
        add_history(f"Division {numbers} = {result}")

    # Modulus
    elif choice == "5":
        a = get_number("Enter First Number: ")
        b = get_number("Enter Second Number: ")

        result = modulus(a, b)

        print("Result:", result)
        add_history(f"{a} % {b} = {result}")

    # Power
    elif choice == "6":
        base = get_number("Enter Base: ")
        exponent = get_number("Enter Exponent: ")

        result = power(base, exponent)

        print("Result:", result)
        add_history(f"{base}^{exponent} = {result}")

    # Square Root
    elif choice == "7":
        number = get_number("Enter Number: ")

        result = square_root(number)

        print("Result:", result)
        add_history(f"√{number} = {result}")

    # Factorial
    elif choice == "8":
        number = int(
            get_number("Enter Number: ")
        )

        result = factorial(number)

        print("Result:", result)
        add_history(f"{number}! = {result}")

    # Logarithm
    elif choice == "9":
        number = get_number("Enter Number: ")

        result = logarithm(number)

        print("Result:", result)
        add_history(f"log({number}) = {result}")

    # GPA
    elif choice == "10":
        count = get_positive_integer(
            "How many courses? "
        )

        courses = []

        for i in range(count):
            grade = input(
                f"Grade of course {i+1}: "
            )

            credits = int(
                get_number(
                    f"Credits of course {i+1}: "
                )
            )

            courses.append({
                "grade": grade,
                "credits": credits
            })

        result = calculate_gpa(courses)

        print("GPA:", result)
        add_history(f"GPA = {result}")

    # CGPA
    elif choice == "11":
        semesters = get_positive_integer(
            "Number of semesters: "
        )

        gpas = []

        for i in range(semesters):
            gpa = get_number(
                f"GPA of semester {i+1}: "
            )

            gpas.append(gpa)

        result = calculate_cgpa(gpas)

        print("CGPA:", result)
        add_history(f"CGPA = {result}")

    # Percentage
    elif choice == "12":
        obtained = get_number(
            "Obtained Marks: "
        )

        total = get_number(
            "Total Marks: "
        )

        result = calculate_percentage(
            obtained,
            total
        )

        print("Percentage:", result)
        add_history(
            f"Percentage = {result}"
        )

    # BMI
    elif choice == "13":
        weight = get_number(
            "Weight (kg): "
        )

        height = get_number(
            "Height (m): "
        )

        bmi = calculate_bmi(
            weight,
            height
        )

        print("BMI:", bmi)

        if isinstance(bmi, float):
            print(
                "Category:",
                bmi_category(bmi)
            )

        add_history(f"BMI = {bmi}")

    # Age
    elif choice == "14":
        year = int(
            get_number(
                "Birth Year: "
            )
        )

        age = calculate_age(year)

        print("Age:", age)
        print("Months:", age_in_months(age))
        print("Days:", age_in_days(age))

        add_history(f"Age = {age}")

    # Area
    elif choice == "15":
        length = get_number("Length: ")
        width = get_number("Width: ")

        result = rectangle_area(
            length,
            width
        )

        print("Area:", result)

        add_history(
            f"Rectangle Area = {result}"
        )

    # Perimeter
    elif choice == "16":
        length = get_number("Length: ")
        width = get_number("Width: ")

        result = rectangle_perimeter(
            length,
            width
        )

        print("Perimeter:", result)

        add_history(
            f"Rectangle Perimeter = {result}"
        )

    # Unit Converter
    elif choice == "17":
        km = get_number(
            "Kilometers: "
        )

        result = km_to_miles(km)

        print("Miles:", result)

        add_history(
            f"{km} km = {result} miles"
        )

    # Currency Converter
    elif choice == "18":
        amount = get_number(
            "Amount: "
        )

        from_currency = input(
            "From Currency: "
        )

        to_currency = input(
            "To Currency: "
        )

        result = convert_currency(
            amount,
            from_currency,
            to_currency
        )

        print("Converted:", result)

        add_history(
            f"{amount} {from_currency} -> "
            f"{to_currency} = {result}"
        )

    # Show History
    elif choice == "19":
        show_history()

    # Clear History
    elif choice == "20":
        clear_history()

    # Exit
    elif choice == "21":
        print(
            "\nThank you for using Calculation Hub."
        )
        break

    else:
        print("\nInvalid Choice.")
