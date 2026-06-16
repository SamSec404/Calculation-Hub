def add(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


def subtract(numbers):

    if len(numbers) == 0:
        return 0

    result = numbers[0]

    for number in numbers[1:]:
        result -= number

    return result


def multiply(numbers):

    if len(numbers) == 0:
        return 0

    result = 1

    for number in numbers:
        result *= number

    return result


def divide(numbers):

    if len(numbers) == 0:
        return 0

    result = numbers[0]

    for number in numbers[1:]:

        if number == 0:
            return "Error: Division by zero"

        result /= number

    return result


def modulus(a, b):

    if b == 0:
        return "Error: Modulus by zero"

    return a % b


def power(base, exponent):
    return base ** exponent