from database.db_manager import get_connection
from Models.room import Room
from Models.guest import Guest


class Reservation:
    def __init__(self, reservation_id, guest_ids, room_id, check_in_date, check_out_date):
        # el function di betet3amel lama te3mel object Reservation gedid
        self.reservation_id = reservation_id
        self.guest_ids = guest_ids  # list of guest ids
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def print_added_object(self):
        # hena ba3mel print lel data b tari2a sadeqa lel beginner
        print("Saved to database: Reservation(reservation_id=", self.reservation_id, ", guest_ids=", self.guest_ids, ", room_id=", self.room_id, ", check_in_date=", self.check_in_date, ", check_out_date=", self.check_out_date, ")")

    def save_to_db(self):
        # di function bet7ot el reservation fel database
        conn = get_connection()
        cursor = conn.cursor()

        # hena by7ot el data fel table reservations
        for guest_id in self.guest_ids:
            cursor.execute(
                '''
                INSERT OR REPLACE INTO reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (self.reservation_id, guest_id, self.room_id, self.check_in_date, self.check_out_date)
            )

        conn.commit()
        conn.close()

        # ba3d ma y7ot el data, by3mel print 3la el object
        self.print_added_object()

    def calculate_payment(self, guests, room):
        # di function bet7seb el total price 3la 7asab el room w el days
        from datetime import datetime
        check_in = datetime.strptime(self.check_in_date, "%Y-%m-%d")
        check_out = datetime.strptime(self.check_out_date, "%Y-%m-%d")
        nights = (check_out - check_in).days
        total_price = nights * room.price_per_night
        # hena momken tzawed discounts aw taxes law 3ayez
        return total_price, None
