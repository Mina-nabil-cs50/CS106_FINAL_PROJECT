import sqlite3

# Function to connect to the SQLite database (or create it if it doesn't exist)
def connect_to_database():
    # Connect to the database file (creates it if it doesn't exist)
    connection = sqlite3.connect("hotel_system.db")
    return connection

# Function to initialize the database and create tables
def initialize_database():
    # Connect to the database
    connection = connect_to_database()
    cursor = connection.cursor()

    # Create the rooms table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number TEXT NOT NULL,
            is_occupied BOOLEAN NOT NULL DEFAULT 0
        )
    ''')

    # Create the guests table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # Create the reservations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_id INTEGER NOT NULL,
            room_id INTEGER NOT NULL,
            check_in_date TEXT NOT NULL,
            check_out_date TEXT NOT NULL,
            total_price REAL NOT NULL,
            FOREIGN KEY (guest_id) REFERENCES guests (id),
            FOREIGN KEY (room_id) REFERENCES rooms (id)
        )
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

# Call the function to initialize the database when the script is run
if __name__ == "__main__":
    initialize_database()