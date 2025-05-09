from database.db_manager import get_connection

class Reservation:
    def __init__(self, reservation_id: int, guest_id: int, room_id: int, check_in_date: str, check_out_date: str):
        self.reservation_id = reservation_id
        self.guest_id = guest_id
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def print_added_object(self):
        """
        Print the object after it is saved to the database.
        """
        print(f"Saved to database: Reservation(reservation_id={self.reservation_id}, guest_id={self.guest_id}, room_id={self.room_id}, check_in_date='{self.check_in_date}', check_out_date='{self.check_out_date}')")

    def save_to_db(self):
        """
        Save the reservation to the database.
        """
        conn = get_connection()
        cursor = conn.cursor()

        # Insert or update the reservation record
        cursor.execute('''
            INSERT OR REPLACE INTO reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.reservation_id, self.guest_id, self.room_id, self.check_in_date, self.check_out_date))

        conn.commit()
        conn.close()

        # Call the function to print the object
        self.print_added_object()
