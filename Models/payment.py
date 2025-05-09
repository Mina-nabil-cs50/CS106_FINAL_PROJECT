from database.db_manager import get_connection
from Models.reservation import Reservation
from datetime import date

class Payment:
    def __init__(self, payment_id: int, reservation: Reservation, payment_date: date, payment_amount: int, is_paid: bool, payment_method: str):
        self.payment_id = payment_id
        self.reservation_id = reservation.reservation_id  # Link to the reservation ID
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

if __name__ == "__main__":
    # Create and save a reservation
    reservation1 = Reservation(1, 1, 1, "2025-03-05", "2025-04-05")
    reservation1.save_to_db()

    # Create a payment linked to the reservation
    payment1 = Payment(
        payment_id=1,
        reservation=reservation1,  # Pass the Reservation object
        payment_date="2025-05-02",
        payment_amount=199,
        is_paid=True,
        payment_method="card"
    )

    # Save the payment to the database
    payment1.save_to_db()
    print("Payment saved to the database.")

    # Query all payments
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payments;")
    payments = cursor.fetchall()
    for payment in payments:
        print(payment)
    conn.close()