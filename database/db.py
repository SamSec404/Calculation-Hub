# database/db.py

import sqlite3


def create_database():

    connection = sqlite3.connect(
        "calculationhub.db"
    )

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        calculation TEXT
    )
    """)

    connection.commit()

    connection.close()
