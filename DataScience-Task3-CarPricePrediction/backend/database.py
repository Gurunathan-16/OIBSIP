import os
import sqlite3
from datetime import datetime


# Task 3 project directory
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Database folder
DATA_DIR = os.path.join(BASE_DIR, "data")

# Create data folder if it doesn't exist
os.makedirs(DATA_DIR, exist_ok=True)

# Database path
DATABASE_PATH = os.path.join(
    DATA_DIR,
    "predictions.db"
)


def get_connection():
    """
    Create a connection to the SQLite database.
    """
    connection = sqlite3.connect(DATABASE_PATH)

    # Allows accessing columns by name
    connection.row_factory = sqlite3.Row

    return connection


def create_table():
    """
    Create prediction history table.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            present_price REAL NOT NULL,
            kms_driven REAL NOT NULL,
            fuel_type TEXT NOT NULL,
            seller_type TEXT NOT NULL,
            transmission TEXT NOT NULL,
            owner INTEGER NOT NULL,
            car_age INTEGER NOT NULL,
            brand TEXT NOT NULL,
            predicted_price REAL NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_prediction(
    present_price,
    kms_driven,
    fuel_type,
    seller_type,
    transmission,
    owner,
    car_age,
    brand,
    predicted_price
):
    """
    Save a prediction to the database.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            present_price,
            kms_driven,
            fuel_type,
            seller_type,
            transmission,
            owner,
            car_age,
            brand,
            predicted_price,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        present_price,
        kms_driven,
        fuel_type,
        seller_type,
        transmission,
        owner,
        car_age,
        brand,
        predicted_price,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()

    connection.close()


def get_predictions():
    """
    Retrieve prediction history.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM predictions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]