from database.db_manager import get_connection

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


# Create and save a reservation
reservation1 = Reservation(1, 1, 1, "2025-03-05", "2025-04-05")

reservation1.save_to_db()

print("Reservation saved to the database.")
