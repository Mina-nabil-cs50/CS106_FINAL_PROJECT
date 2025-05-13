from database.db_manager import get_connection

class Room:
    season = "summer"  # Default season

    def __init__(self, room_id: int, room_type: str, room_floor: int, room_number: str, price_per_night: float, available: bool):
        self.room_id = room_id
        self.room_type = room_type
        self.room_floor = room_floor
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.available = available

    @classmethod
    def change_season(cls, new_season: str):
        cls.season = new_season  # Update the class-level season attribute
        print("Season changed to", cls.season)

        # Update the season in the database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE settings SET season = ? WHERE id = 1", (cls.season,))
        conn.commit()
        conn.close()

    def mark_as_occupied(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def get_room_info(self):
        return {
            "Room ID": self.room_id,
            "Room Type": self.room_type,
            "Room Floor": self.room_floor,
            "Room Number": self.room_number,
            "Price Per Night": self.price_per_night,
            "Available": self.available
        }

    def print_added_object(self):
        """
        Print the object after it is saved to the database.
        """
        print(f"Saved to database: Room(room_id={self.room_id}, room_type='{self.room_type}', room_floor={self.room_floor}, room_number='{self.room_number}', price_per_night={self.price_per_night}, available={self.available}")

    def save_to_db(self):
        """
        Save the room to the database.
        """
        conn = get_connection()
        cursor = conn.cursor()

        # Insert or update the room record
        cursor.execute('''
            INSERT OR REPLACE INTO rooms (room_id, room_number, room_type, room_floor, price_per_night, is_occupied)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.room_id, self.room_number, self.room_type, self.room_floor, self.price_per_night, int(not self.available)))

        conn.commit()
        conn.close()

        # Call the function to print the object
        self.print_added_object()

