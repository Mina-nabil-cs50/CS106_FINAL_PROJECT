from Models.guest import Guest
from Models.reservation import Reservation
from Models.payment import Payment
from database.db_manager import get_connection  


class Staff:
    def __init__(self, staff_id: int, staff_name: str, staff_age: int, staff_role: str = "staff"):
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.staff_age = staff_age
        self.staff_role = staff_role  

    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute((self.staff_id, self.staff_name, self.staff_age, self.staff_role))

        conn.commit()
        conn.close()
        print("Saved to database: Staff(staff_id=",self.staff_id, "staff_name=",self.staff_name, "staff_age=",self.staff_age, "staff_role=",self.staff_role,")")


def staff_functions():
    print("\n Staff Functions ")
    print("1. Add a New Guest")
    print("2. Add a New Reservation")
    print("3. Add a New Payment")
    print("4. Delete a Reservation")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        # Add a Guest
        print("\n Add a Guest ")
        guest_id = int(input("Enter Guest ID: "))
        full_name = input("Enter Full Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        id_document = input("Enter ID Document: ")
        guest_age = int(input("Enter Guest Age: "))
        guest = Guest(guest_id, full_name, phone_number, email, id_document, guest_age)
        guest.save_to_db()
        print("Guest added successfully!")
    elif choice == "2":
        print("\n Add a Reservation ")
        reservation_id = int(input("Enter Reservation ID: "))
        guest_id = int(input("Enter Guest ID for the Reservation: "))
        room_id = int(input("Enter Room ID for the Reservation: "))
        check_in_date = input("Enter Check-In Date (YYYY-MM-DD): ")
        check_out_date = input("Enter Check-Out Date (YYYY-MM-DD): ")
        reservation = Reservation(reservation_id, [guest_id], room_id, check_in_date, check_out_date)
        reservation.save_to_db()
        print("Reservation added successfully!")
    elif choice == "3":
        print("\n Add a Payment ")
        payment_id = int(input("Enter Payment ID: "))
        reservation_id = int(input("Enter Reservation ID for the Payment: "))
        payment_date = input("Enter Payment Date (YYYY-MM-DD): ")
        payment_amount = float(input("Enter Payment Amount: "))
        is_paid = input("Is the payment completed? (yes/no): ").lower() == "yes"
        payment_method = input("Enter Payment Method (e.g., Credit Card, Cash): ")
        payment = Payment(payment_id, reservation_id, payment_date, payment_amount, is_paid, payment_method)
        payment.save_to_db()
        print("Payment added successfully!")
    elif choice == "4":
        print("\n Delete a Reservation ")
        reservation_id = int(input("Enter the Reservation ID to delete: "))
        delete_reservation(reservation_id)
    else:
        print("Invalid choice. Returning to main menu.")


def delete_reservation(reservation_id):

    conn = get_connection()
    cursor = conn.cursor()

    reservation = cursor.fetchone()
    if reservation:
        cursor.execute("DELETE FROM reservations WHERE reservation_id = ?", (reservation_id,))
        conn.commit()
        print("Reservation with ID",reservation_id," has been deleted successfully.")
    else:
        print("No reservation found with ID",reservation_id)

    conn.close()


def edit_guest(guest_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute((guest_id,))
    guest = cursor.fetchone()
    if guest:
        print("Current Info: ID=",guest[0], "Name=",guest[1], "Phone=",guest[2], "Email=",guest[3], "ID Document=",guest[4])
        new_name = input("Enter new name (leave blank to keep current): ")
        new_phone = input("Enter new phone number (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")
        new_id_document = input("Enter new ID document (leave blank to keep current): ")

        updated_name = new_name if new_name else guest[1]
        updated_phone = new_phone if new_phone else guest[2]
        updated_email = new_email if new_email else guest[3]
        updated_id_document = new_id_document if new_id_document else guest[4]

        cursor.execute((updated_name, updated_phone, updated_email, updated_id_document, guest_id))

        conn.commit()
        print("Guest with ID",guest_id,"has been updated successfully")
    else:
        print("No guest found with ID", guest_id)

    conn.close()


def remove_guest(guest_id):

    conn = get_connection()
    cursor = conn.cursor()

    # Check if the guest exists
    cursor.execute((guest_id,))
    guest = cursor.fetchone()
    if guest:
        # Delete the guest
        cursor.execute((guest_id,))
        conn.commit()
        print("Guest with ID", guest_id,"has been removed successfully.")
    else:
        print("No guest found with ID", guest_id)

    conn.close()

