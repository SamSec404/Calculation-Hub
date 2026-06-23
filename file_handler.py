# utils/file_handler.py

def save_to_file(filename, text):

    with open(filename, "a") as file:

        file.write(text + "\n")


def read_file(filename):

    try:

        with open(filename, "r") as file:

            return file.readlines()

    except FileNotFoundError:

        return []