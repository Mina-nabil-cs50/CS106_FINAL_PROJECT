import sqlite3
from database.db_manager import get_connection
from Models.guest import Guest
from Models.reservation import Reservation
from Models.payment import Payment
from Models.admin import admin_functions  # Import admin functions
from Models.staff import staff_functions  # Import staff functions
import datetime


def print_all_rooms():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()
    print("\n--- All Rooms ---")
    print(f"{'ID':<4} {'Number':<8} {'Type':<20} {'Floor':<5} {'Price':<8} {'Occupied':<9}")
    print("-" * 60)
    for room in rooms:
        print(f"{room[0]:<4} {room[1]:<8} {room[2]:<20} {room[3]:<5} {room[4]:<8.2f} {'Yes' if room[5] else 'No':<9}")
    conn.close()

def print_all_guests():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM guests")
    guests = cursor.fetchall()
    print("\n--- All Guests ---")
    for guest in guests:
        print(f"Guest ID: {guest[0]}, Name: {guest[1]}, Phone: {guest[2]}, Email: {guest[3]}, ID Doc: {guest[4]}, Age: {guest[5]}")
    conn.close()

def print_all_reservations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    print("\n--- All Reservations ---")
    for res in reservations:
        print(f"Reservation ID: {res[0]}, Guest ID: {res[1]}, Room ID: {res[2]}, Check-in: {res[3]}, Check-out: {res[4]}")
    conn.close()

def print_ongoing_reservations():
    conn = get_connection()
    cursor = conn.cursor()
    today = datetime.date.today().isoformat()
    cursor.execute(
        "SELECT * FROM reservations WHERE check_in_date <= ? AND check_out_date >= ?",
        (today, today)
    )
    reservations = cursor.fetchall()
    print("\n--- Ongoing Reservations ---")
    if not reservations:
        print("No ongoing reservations.")
    for res in reservations:
        print(f"Reservation ID: {res[0]}, Guest ID: {res[1]}, Room ID: {res[2]}, Check-in: {res[3]}, Check-out: {res[4]}")
    conn.close()

def add_reservation_menu():
    print("\n--- Add Reservation ---")
    # Add Guest(s)
    guests = []
    while True:
        print("\nEnter Guest Information:")
        guest_id = int(input("Guest ID: "))
        full_name = input("Full Name: ")
        phone_number = input("Phone Number: ")
        email = input("Email: ")
        id_document = input("ID Document: ")
        guest_age = int(input("Guest Age: "))
        guest = Guest(guest_id, full_name, phone_number, email, id_document, guest_age)
        guest.save_to_db()
        guests.append(guest)
        more = input("Add another guest? (y/n): ").lower()
        if more != "y":
            break

    # Show all available rooms and types
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT room_id, room_number, room_type, room_floor, price_per_night, is_occupied FROM rooms")
    rooms = cursor.fetchall()
    if not rooms:
        print("No rooms available in the system. Please add rooms first.")
        conn.close()
        return

    # Print all rooms BEFORE asking for Room ID
    print("\nAvailable Rooms:")
    for room in rooms:
        print(f"Room ID: {room[0]}, Number: {room[1]}, Type: {room[2]}, Floor: {room[3]}, Price: {room[4]}, Occupied: {'Yes' if room[5] else 'No'}")

    # Show all unique room types
    cursor.execute("SELECT DISTINCT room_type FROM rooms")
    room_types = [row[0] for row in cursor.fetchall()]
    print("\nAvailable Room Types:")
    for idx, rtype in enumerate(room_types, 1):
        print(f"{idx}. {rtype}")

    # Let user pick a room by ID
    room_id = int(input("Enter the Room ID you want to reserve: "))
    cursor.execute("SELECT * FROM rooms WHERE room_id = ?", (room_id,))
    selected_room = cursor.fetchone()
    if not selected_room:
        print("Invalid Room ID.")
        conn.close()
        return

    # Use the selected room's info
    room_type = selected_room[2]
    room_floor = selected_room[3]
    room_number = selected_room[1]
    price_per_night = selected_room[4]
    available = not selected_room[5]
    conn.close()

    # Create and save the room (if you want to update its status, etc.)
    from Models.room import Room
    room = Room(room_id, room_type, room_floor, room_number, price_per_night, available)
    room.save_to_db()

    # Add Reservation
    reservation_id = int(input("\nReservation ID: "))
    check_in_date = input("Check-in Date (YYYY-MM-DD): ")
    check_out_date = input("Check-out Date (YYYY-MM-DD): ")
    guest_ids = [g.guest_id for g in guests]
    reservation = Reservation(reservation_id, guest_ids, room_id, check_in_date, check_out_date)
    reservation.save_to_db()
    print("Reservation added successfully!")

    # Calculate Payment Automatically
    total_price, payments = reservation.calculate_payment(guests, room)
    print(f"Calculated total payment amount: {total_price}")

    # Add Payment
    payment_id = int(input("\nPayment ID: "))
    payment_date = input("Payment Date (YYYY-MM-DD): ")
    is_paid = input("Is the payment completed? (yes/no): ").lower() == "yes"
    payment_method = input("Payment Method (e.g., Credit Card, Cash): ")
    payment = Payment(payment_id, reservation_id, payment_date, total_price, is_paid, payment_method)
    payment.save_to_db()
    print("Payment added successfully!")


def delete_all_data():
    conn = get_connection()
    cursor = conn.cursor()
    # Disable foreign key checks temporarily to avoid constraint errors
    cursor.execute("PRAGMA foreign_keys = OFF;")
    # List all your tables here
    tables = ["guests", "rooms", "reservations", "payments", "staff", "settings"]
    for table in tables:
        cursor.execute(f"DELETE FROM {table};")
    conn.commit()
    cursor.execute("PRAGMA foreign_keys = ON;")
    conn.close()
    print("All data deleted from all tables.")


def staff_menu():
    while True:
        print("\n--- Staff Functions ---")
        print("1. Add Reservation")
        print("2. Print All Rooms Info")
        print("3. Print All Guests Info")
        print("4. Print All Reservations Info")
        print("5. Print All Ongoing Reservations")
        print("6. Exit to Main Menu")
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            add_reservation_menu()
        elif choice == "2":
            print_all_rooms()
        elif choice == "3":
            print_all_guests()
        elif choice == "4":
            print_all_reservations()
        elif choice == "5":
            print_ongoing_reservations()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


#Define el function el ra2esiya bta3t el menu
def main_menu():
    while True:
        print("\nHotel Management System ")
        print("-------------------------------")
        print("1. Admin Functions")
        print("2. Staff Functions")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            admin_functions()
        elif choice == "2":
            staff_menu()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


#Check law el file da etran directly
if __name__ == "__main__":
    #Call el main_menu function 3shan el program yebda2 men el menu el ra2esi
    main_menu()

