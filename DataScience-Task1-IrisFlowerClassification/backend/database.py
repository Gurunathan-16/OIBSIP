import sqlite3
import os
from datetime import datetime


# Get the project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create the data directory if it doesn't exist
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

# Database file path
DB_PATH = os.path.join(DATA_DIR, "predictions.db")


def get_connection():
    """Create and return a database connection."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """Create the predictions table if it doesn't exist."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sepal_length REAL NOT NULL,
            sepal_width REAL NOT NULL,
            petal_length REAL NOT NULL,
            petal_width REAL NOT NULL,
            prediction TEXT NOT NULL,
            confidence REAL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully!")


def save_prediction(
    sepal_length,
    sepal_width,
    petal_length,
    petal_width,
    prediction,
    confidence
):
    """Save a prediction to the database."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            sepal_length,
            sepal_width,
            petal_length,
            petal_width,
            prediction,
            confidence,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        sepal_length,
        sepal_width,
        petal_length,
        petal_width,
        prediction,
        confidence,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    prediction_id = cursor.lastrowid
    connection.close()

    return prediction_id


def get_prediction_history():
    """Retrieve all predictions from newest to oldest."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM predictions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    connection.close()

    # Convert SQLite rows into dictionaries
    return [dict(row) for row in rows]