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

    for index, record in enumerate(records, start=1):
        print(f"{index}. {record.strip()}")


def clear_history():

    with open(HISTORY_FILE, "w") as file:
        pass

    print("\nHistory cleared successfully.")
