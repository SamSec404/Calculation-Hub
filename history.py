# utils/history.py

history = []


def add_history(record):
    history.append(record)


def show_history():

    if len(history) == 0:

        print("\nNo calculations found.")
        return

    print("\n===== HISTORY =====")

    for index, item in enumerate(history, start=1):
        print(f"{index}. {item}")


def clear_history():

    history.clear()

    print("\nHistory cleared successfully.")

from utils.file_handler import save_to_file
from utils.file_handler import read_file

HISTORY_FILE = "data/history.txt"


def add_history(record):

    save_to_file(HISTORY_FILE, record)


def show_history():

    records = read_file(HISTORY_FILE)

    if not records:

        print("\nNo history found.")
        return

    print("\n===== HISTORY =====")

    for record in records:

        print(record.strip())
