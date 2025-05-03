from Database.db_manager import get_connection

class Reservation:
    def __init__(self, reservation_id:int, guest_id:int, room_id:int, check_in_date:str, check_out_date:str):
        self.reservation_id = reservation_id
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def save_to_db(self):
        """
        Save the reservation to the database.
        """
        print(f"Saving reservation: {self.reservation_id}, Guest ID: {self.guest_id}, Room ID: {self.room_id}")
        conn = get_connection()
        cursor = conn.cursor()

        # Insert or update the reservation record
        cursor.execute('''
            INSERT OR REPLACE INTO reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.reservation_id, self.guest_id, self.room_id, self.check_in_date, self.check_out_date))

        conn.commit()
        conn.close()
        print("Reservation saved successfully.")

    @classmethod
    def load_from_db(cls, reservation_id):
        """
        Load a reservation from the database by reservation_id.
        """
        conn = get_connection()
        cursor = conn.cursor()

        # Query the reservation record
        cursor.execute('SELECT * FROM reservations WHERE reservation_id = ?', (reservation_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            # Create and return a Reservation object
            return cls(reservation_id=row[0], guest_id=row[1], room_id=row[2], check_in_date=row[3], check_out_date=row[4])
        else:
            return None

# Create and save a reservation
reservation1 = Reservation(1, 1, 1, "2025-03-05", "2025-04-05")

reservation1.save_to_db()

print("Reservation saved to the database.")
