from database.db_manager import get_connection
from Models.reservation import Reservation
from Models.room import Room
from Models.guest import Guest


class Payment:
    def __init__(self, payment_id: int, reservation_id: int, payment_date: str, payment_amount: float, is_paid: bool, payment_method: str):
        self.payment_id = payment_id
        self.reservation_id = reservation_id
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.is_paid = is_paid
        self.payment_method = payment_method

    def calculate_payment(self, reservation: Reservation, guests: list[Guest], room: Room):
        """
        Calculate the payment amount using the reservation and room details.
        """
        total_price, payments = reservation.calculate_payment(guests, room)
        self.payment_amount = total_price
        return payments

    def save_to_db(self):
        """
        Save the payment to the database.
        """
        conn = get_connection()
        cursor = conn.cursor()

        # Insert or update the payment record
        cursor.execute('''
            INSERT OR REPLACE INTO payments (payment_id, reservation_id, payment_date, payment_amount, is_paid, payment_method)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.payment_id, self.reservation_id, self.payment_date, self.payment_amount, int(self.is_paid), self.payment_method))

        conn.commit()
        conn.close()
