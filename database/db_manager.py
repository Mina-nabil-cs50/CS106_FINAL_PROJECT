import sqlite3
import os

DB_PATH = "C:/Users/hanat/Desktop/College/CS106_FINAL_PROJECT/database/hotel.db"  # Path to your SQLite database file

def get_connection():
    return sqlite3.connect(DB_PATH)

def setup_database():
    schema_file = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_file, "r") as f:
        sql_script = f.read()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(sql_script)
    conn.commit()
    conn.close()
    print(" Database setup complete.")

if __name__ == "__main__":
    setup_database()
print("ran")
