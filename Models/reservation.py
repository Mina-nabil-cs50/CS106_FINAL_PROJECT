from database.db_manager import get_connection
from Models.room import Room
from Models.guest import Guest


class Reservation:
    def __init__(self, reservation_id: int, guest_ids: list[int], room_id: int, check_in_date: str, check_out_date: str):
        self.reservation_id = reservation_id
        self.guest_ids = guest_ids
        self.room_id = room_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def calculate_payment(self, guests: list[Guest], room: Room):
        total_price = room.price_per_night * len(guests)#calculates the total price depending on 2ad eah guests f el reservation

        if room.season.lower() == "summer":
            total_price *= 1.25

        age_distribution = {"child": 0.5,"adult": 1.0,"senior": 0.75}

        payments = {}
        for guest in guests:
            if guest.guest_age < 12:
                payments[guest.full_name] = total_price * age_distribution["child"] / len(guests)
            elif guest.guest_age >= 60:
                payments[guest.full_name] = total_price * age_distribution["senior"] / len(guests)
            else:
                payments[guest.full_name] = total_price * age_distribution["adult"] / len(guests)

        return total_price, payments

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()

    
        main_guest_id = self.guest_ids[0] if self.guest_ids else None
        cursor.execute(
            '''
            INSERT OR REPLACE INTO reservations (reservation_id, guest_id, room_id, check_in_date, check_out_date)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (self.reservation_id, main_guest_id, self.room_id, self.check_in_date, self.check_out_date)
        )

        # If you have a reservation_guests linking table, you would insert all guest_ids here.

        conn.commit()
        conn.close()
