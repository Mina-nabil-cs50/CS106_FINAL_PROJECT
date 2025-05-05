from database.db_manager import get_connection
from Models.reservation import Reservation
from datetime import date

class Payment:
    def __init__(self, payment_id: int, reservation_id: int, payment_date: date, payment_amount: int, is_paid: bool, payment_method: str):
        self.payment_id = payment_id
        self.reservation_id = reservation_id  # Store the reservation ID directly
        self.payment_date = payment_date
        self.payment_amount = payment_amount
        self.is_paid = is_paid
        self.payment_method = payment_method

    def confirm_payment(self):
        self.is_paid = True
        reservation = Reservation.load_from_db(self.reservation_id)
        if reservation:
            reservation.is_paid = True
            reservation.save_to_db()

    def generate_receipt(self):
        print(f"Payment ID: {self.payment_id}")
        print(f"Reservation ID: {self.reservation_id}")
        print(f"Payment Date: {self.payment_date}")
        print(f"Payment Amount: {self.payment_amount}")
        print(f"Is Paid: {self.is_paid}")
        print(f"Payment Method: {self.payment_method}")

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




payment1 = Payment(
    payment_id=1,
    reservation_id=0,  
    payment_date="2025-05-02",
    payment_amount=199,
    is_paid=True,
    payment_method="card"
)

#
payment1.save_to_db()
print("Payment saved to the database.")


