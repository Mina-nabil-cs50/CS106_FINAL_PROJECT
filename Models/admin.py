from Models.room import Room
from Models.guest import Guest
from Models.staff import Staff
from database.db_manager import get_connection


class Admin(Staff):
    def __init__(self, staff_id: int, staff_name: str, staff_age: int):
        super().__init__(staff_id, staff_name, staff_age, staff_role="admin")  # Automatically set staff_role to "admin"
     
    def save_to_db(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT OR REPLACE INTO staff (staff_id, staff_name, staff_age, staff_role)
            VALUES (?, ?, ?, ?)
        ''', (self.staff_id, self.staff_name, self.staff_age, self.staff_role))

        conn.commit()  # Ensure changes are saved
        conn.close()


# Ensure Admin and Default Staff Exist in the Database
def ensure_admin_and_staff():
    """
    Ensure that at least one admin and one default staff member exist in the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    print("Checking if default admin exists...")
    # Check if the Admin exists
    cursor.execute("SELECT * FROM staff WHERE staff_role = 'admin'")
    admin = cursor.fetchone()
    if not admin:
        # Add a default Admin
        default_admin = Admin(1, "Admin", 30)
        default_admin.save_to_db()
        print("Default Admin added to the database.")

    print("Checking if default staff exists...")
    # Check if a default Staff exists
    cursor.execute("SELECT * FROM staff WHERE staff_role = 'staff'")
    staff = cursor.fetchone()
    if not staff:
        # Add a default Staff member
        default_staff = Staff(2, "Default Staff", 25)
        default_staff.save_to_db()
        print("Default Staff added to the database.")

    conn.close()


def admin_functions():
    ensure_admin_and_staff()  # Ensure Admin and Staff exist before showing the menu

    print("\n--- Admin Functions ---")
    print("1. Add a New Room")
    print("2. Add 50 Predefined Rooms")
    print("3. Edit a Room")
    print("4. Remove a Room")
    print("5. Add a New Staff Member")
    print("6. Edit a Staff Member")
    print("7. Remove a Staff Member")
    print("8. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ").strip()

    if choice == "1":
        # Add a Room
        print("\n--- Add a Room ---")
        room_id = int(input("Enter Room ID: "))
        room_type = input("Enter Room Type (e.g., Single, Double, Suite): ")
        room_floor = int(input("Enter Room Floor: "))
        room_number = input("Enter Room Number: ")
        price_per_night = float(input("Enter Price Per Night: "))
        available = input("Is the room available? (yes/no): ").strip().lower() == "yes"
        room = Room(room_id, room_type, room_floor, room_number, price_per_night, available)
        room.save_to_db()
        print("Room added successfully!")
    elif choice == "2":
        # Add 50 Predefined Rooms
        print("\n--- Adding 50 Predefined Rooms ---")
        for i in range(1, 51):
            room = Room(
                room_id=i,
                room_type="Single" if i % 2 == 0 else "Double",
                room_floor=(i // 10) + 1,
                room_number=f"{(i // 10) + 1}{i % 10:02}",
                price_per_night=50.0 + (i % 5) * 10,
                available=True,
            )
            room.save_to_db()
        print("50 rooms added successfully!")
    elif choice == "3":
        # Edit a Room
        print("\n--- Edit a Room ---")
        room_id = int(input("Enter the Room ID to edit: "))
        edit_room(room_id)
    elif choice == "4":
        # Remove a Room
        print("\n--- Remove a Room ---")
        room_id = int(input("Enter the Room ID to remove: "))
        remove_room(room_id)
    elif choice == "5":
        # Add a New Staff Member
        print("\n--- Add a New Staff Member ---")
        staff_id = int(input("Enter Staff ID: "))
        staff_name = input("Enter Staff Name: ")
        staff_age = int(input("Enter Staff Age: "))
        staff_role = input("Enter Staff Role: ")
        staff = Staff(staff_id, staff_name, staff_age, staff_role)
        staff.save_to_db()
        print("Staff member added successfully!")
    elif choice == "6":
        # Edit a Staff Member
        print("\n--- Edit a Staff Member ---")
        staff_id = int(input("Enter the Staff ID to edit: "))
        edit_staff(staff_id)
    elif choice == "7":
        # Remove a Staff Member
        print("\n--- Remove a Staff Member ---")
        staff_id = int(input("Enter the Staff ID to remove: "))
        remove_staff(staff_id)
    elif choice == "8":
        return
    else:
        print("Invalid choice. Returning to main menu.")


def edit_room(room_id):
    """
    Edit a room's details in the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the room exists
    cursor.execute("SELECT * FROM rooms WHERE room_id = ?", (room_id,))
    room = cursor.fetchone()
    if room:
        print(f"Current Info: ID={room[0]}, Type={room[1]}, Floor={room[2]}, Number={room[3]}, Price={room[4]}, Available={bool(room[5])}")
        new_type = input("Enter new room type (leave blank to keep current): ").strip()
        new_floor = input("Enter new floor (leave blank to keep current): ").strip()
        new_number = input("Enter new room number (leave blank to keep current): ").strip()
        new_price = input("Enter new price per night (leave blank to keep current): ").strip()
        new_available = input("Is the room available? (yes/no, leave blank to keep current): ").strip().lower()

        # Update only the fields that are provided
        updated_type = new_type if new_type else room[1]
        updated_floor = int(new_floor) if new_floor else room[2]
        updated_number = new_number if new_number else room[3]
        updated_price = float(new_price) if new_price else room[4]
        updated_available = new_available == "yes" if new_available else bool(room[5])

        # Update the room record in the database
        cursor.execute('''
            UPDATE rooms
            SET room_type = ?, room_floor = ?, room_number = ?, price_per_night = ?, is_occupied = ?
            WHERE room_id = ?
        ''', (updated_type, updated_floor, updated_number, updated_price, int(not updated_available), room_id))

        conn.commit()
        print(f"Room with ID {room_id} has been updated successfully.")
    else:
        print(f"No room found with ID {room_id}.")

    conn.close()


def remove_room(room_id):
    """
    Remove a room from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the room exists
    cursor.execute("SELECT * FROM rooms WHERE room_id = ?", (room_id,))
    room = cursor.fetchone()
    if room:
        # Delete the room
        cursor.execute("DELETE FROM rooms WHERE room_id = ?", (room_id,))
        conn.commit()
        print(f"Room with ID {room_id} has been removed successfully.")
    else:
        print(f"No room found with ID {room_id}.")

    conn.close()


def edit_staff(staff_id):
    """
    Edit a staff member's details in the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the staff member exists
    cursor.execute("SELECT * FROM staff WHERE staff_id = ?", (staff_id,))
    staff = cursor.fetchone()
    if staff:
        print(f"Current Info: ID={staff[0]}, Name={staff[1]}, Age={staff[2]}, Role={staff[3]}")
        new_name = input("Enter new name (leave blank to keep current): ").strip()
        new_age = input("Enter new age (leave blank to keep current): ").strip()
        new_role = input("Enter new role (leave blank to keep current): ").strip()

        # Update only the fields that are provided
        updated_name = new_name if new_name else staff[1]
        updated_age = int(new_age) if new_age else staff[2]
        updated_role = new_role if new_role else staff[3]

        # Update the staff record in the database
        cursor.execute('''
            UPDATE staff
            SET staff_name = ?, staff_age = ?, staff_role = ?
            WHERE staff_id = ?
        ''', (updated_name, updated_age, updated_role, staff_id))

        conn.commit()
        print(f"Staff member with ID {staff_id} has been updated successfully.")
    else:
        print(f"No staff member found with ID {staff_id}.")

    conn.close()


def remove_staff(staff_id):
    """
    Remove a staff member from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the staff member exists
    cursor.execute("SELECT * FROM staff WHERE staff_id = ?", (staff_id,))
    staff = cursor.fetchone()
    if staff:
        # Delete the staff member
        cursor.execute("DELETE FROM staff WHERE staff_id = ?", (staff_id,))
        conn.commit()
        print(f"Staff member with ID {staff_id} has been removed successfully.")
    else:
        print(f"No staff member found with ID {staff_id}.")

    conn.close()
print("admin model ran sucsessfully ")

if __name__ == "__main__":
    # Test Admin
    admin = Admin(1, "Admin", 30)  # No need to pass staff_role
    admin.save_to_db()

    # Test Staff
    staff = Staff(2, "Default Staff", 25)
    staff.save_to_db()