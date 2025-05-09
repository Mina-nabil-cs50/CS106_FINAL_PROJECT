from database.db_manager import get_connection
from datetime import date    

class Reservation:
    def __init__(self, reservation_id: int, guest_id: int, room_id: int, check_in_date: date, check_out_date: date):
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
        print(f"Reservation {self.reservation_id} saved successfully.")

# Create and save 10 reservations
reservations = [
    Reservation(1, 1, 101, "2025-03-01", "2025-03-05"),
    Reservation(2, 2, 102, "2025-03-06", "2025-03-10"),
    Reservation(3, 3, 103, "2025-03-11", "2025-03-15"),
    Reservation(4, 4, 104, "2025-03-16", "2025-03-20"),
    Reservation(5, 5, 105, "2025-03-21", "2025-03-25"),
    Reservation(6, 6, 106, "2025-03-26", "2025-03-30"),
    Reservation(7, 7, 107, "2025-04-01", "2025-04-05"),
    Reservation(8, 8, 108, "2025-04-06", "2025-04-10"),
    Reservation(9, 9, 109, "2025-04-11", "2025-04-15"),
    Reservation(10, 10, 110, "2025-04-16", "2025-04-20"),
]

for reservation in reservations:
    reservation.save_to_db()

print("All reservations saved to the database.")
