import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "predictions.db"
)


def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)


def create_table():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            prediction TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(message, prediction):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions
        (message, prediction, created_at)
        VALUES (?, ?, ?)
        """,
        (
            message,
            prediction,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()


def get_predictions():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, message, prediction, created_at
        FROM predictions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows