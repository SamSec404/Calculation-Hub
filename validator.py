# utils/validator.py

def get_number(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("Invalid input.")


def get_positive_integer(message):

    while True:

        try:
            value = int(input(message))

            if value > 0:
                return value

            print("Enter a positive integer.")

        except ValueError:
            print("Invalid input.")
