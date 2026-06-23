from Calculators.basic_calc import add
from Calculators.basic_calc import subtract
from Calculators.basic_calc import multiply
from Calculators.basic_calc import divide
from Calculators.basic_calc import modulus
from Calculators.basic_calc import power

from Utils.history import add_history
from Utils.history import show_history
from Utils.history import clear_history

from Utils.validator import get_number
from Utils.validator import get_positive_integer


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
    print("7. Show History")
    print("8. Clear History")
    print("9. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":

        numbers = get_numbers()

        result = add(numbers)

        operation = f"Addition {numbers} = {result}"

        print("Result:", result)

        add_history(operation)

    elif choice == "2":

        numbers = get_numbers()

        result = subtract(numbers)

        operation = f"Subtraction {numbers} = {result}"

        print("Result:", result)

        add_history(operation)

    elif choice == "3":

        numbers = get_numbers()

        result = multiply(numbers)

        operation = f"Multiplication {numbers} = {result}"

        print("Result:", result)

        add_history(operation)

    elif choice == "4":

        numbers = get_numbers()

        result = divide(numbers)

        operation = f"Division {numbers} = {result}"

        print("Result:", result)

        add_history(operation)

    elif choice == "5":

        a = get_number("Enter First Number: ")
        b = get_number("Enter Second Number: ")

        result = modulus(a, b)

        operation = f"{a} % {b} = {result}"

        print("Result:", result)

        add_history(operation)

    elif choice == "6":

        base = get_number("Enter Base: ")

        exponent = get_number("Enter Exponent: ")

        result = power(base, exponent)

        operation = f"{base}^{exponent} = {result}"

        print("Result:", result)

        add_history(operation)

    elif choice == "7":

        show_history()

    elif choice == "8":

        clear_history()

    elif choice == "9":

        print("\nThank you for using Calculation Hub.")
        break

    else:

        print("\nInvalid Choice.")