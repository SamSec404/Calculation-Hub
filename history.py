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