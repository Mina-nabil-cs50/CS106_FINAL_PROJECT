import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "hotel.db")  

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    return sqlite3.connect(DB_PATH)

def setup_database():
    schema_file = os.path.join(BASE_DIR, "schema.sql")
    if not os.path.exists(schema_file):
        raise FileNotFoundError("Missing schema file at", schema_file)

    with open(schema_file, "r") as f:
        sql_script = f.read()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()
    print("ran")
